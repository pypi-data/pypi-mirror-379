# SPDX-FileCopyrightText: 2025 Espressif Systems (Shanghai) CO LTD
# SPDX-License-Identifier: Apache-2.0

import io
import logging
import os.path
import typing as t
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path

import pytest
from _pytest.config import ExitCode

from idf_ci._compat import UNDEF, UndefinedOr, is_undefined
from idf_ci.envs import GitlabEnvVars
from idf_ci.settings import get_ci_settings

from ..utils import remove_subfolders, setup_logging
from .models import PytestCase
from .plugin import IdfPytestPlugin

logger = logging.getLogger(__name__)


def get_pytest_cases(
    *,
    paths: t.Optional[t.List[str]] = None,
    target: str = 'all',
    sdkconfig_name: t.Optional[str] = None,
    marker_expr: UndefinedOr[t.Optional[str]] = UNDEF,
    filter_expr: t.Optional[str] = None,
) -> t.List[PytestCase]:
    """Collect pytest test cases from specified paths.

    :param paths: List of file system paths to collect test cases from
    :param target: Filter by targets
    :param sdkconfig_name: Filter tests whose apps are built with this sdkconfig name
    :param marker_expr: Filter by pytest marker expression -m
    :param filter_expr: Filter by pytest filter expression -k

    :returns: List of collected PytestCase objects

    :raises RuntimeError: If pytest collection fails
    """
    envs = GitlabEnvVars()

    paths = paths or ['.']

    if is_undefined(marker_expr):
        marker_expr = 'host_test' if 'linux' in target else 'not host_test'

    if filter_expr is None:
        filter_expr = envs.IDF_CI_SELECT_BY_FILTER_EXPR

    plugin = IdfPytestPlugin(
        cli_target=target,
        sdkconfig_name=sdkconfig_name,
    )

    check_dirs = []
    not_in_folders = [Path(f).resolve() for f in get_ci_settings().exclude_dirs]
    for folder in remove_subfolders(paths):
        for not_in_folder in not_in_folders:
            if not_in_folder == folder or not_in_folder in folder.parents:
                logger.debug(
                    'Skipping folder %s because it was excluded by %s',
                    folder,
                    not_in_folder,
                )
                break
        else:
            check_dirs.append(str(folder))

    args = [
        # remove sub folders if parent folder is already in the list
        # https://github.com/pytest-dev/pytest/issues/13319
        *check_dirs,
        '--collect-only',
        '--rootdir',
        os.getcwd(),
        '--target',
        target,
    ]

    if marker_expr:
        args.extend(['-m', f'{marker_expr}'])
    if filter_expr:
        args.extend(['-k', f'{filter_expr}'])

    logger.debug('Collecting pytest test cases with args: %s', args)

    original_log_level = logger.parent.level  # type: ignore
    with io.StringIO() as stdout_buffer, io.StringIO() as stderr_buffer:
        with redirect_stdout(stdout_buffer), redirect_stderr(stderr_buffer):
            result = pytest.main(args, plugins=[plugin])
        stdout_content = stdout_buffer.getvalue()
        stderr_content = stderr_buffer.getvalue()

    # Restore logging level as redirection changes it
    setup_logging(level=original_log_level)

    # args is modified by pytest.main
    if 'no:idf-ci' in args:
        logging.debug('Ignoring result from args `%s` because it contains no:idf-ci marker', args)
        return []

    if 'no:pytest-embedded' in args:
        logging.debug('Ignoring result from args `%s` because it contains no:pytest-embedded marker', args)
        return []

    if result == ExitCode.OK:
        return plugin.cases

    raise RuntimeError(f'pytest collection failed.\nArgs: {args}\nStdout: {stdout_content}\nStderr: {stderr_content}')
