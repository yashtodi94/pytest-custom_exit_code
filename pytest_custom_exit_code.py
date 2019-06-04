# -*- coding: utf-8 -*-

import pytest


def pytest_addoption(parser):
    group = parser.getgroup('custom_exit_code')
    group.addoption(
        '--suppress-no-test-exit-code',
        action='store_true',
        default=False,
        help='Suppress the "no tests collected" exit code.'
    )


@pytest.hookimpl(trylast=True)
def pytest_sessionfinish(session, exitstatus):
    if session.config.getoption('--suppress-no-test-exit-code'):
        from _pytest.main import EXIT_NOTESTSCOLLECTED, EXIT_OK
        if exitstatus == EXIT_NOTESTSCOLLECTED:
            session.exitstatus = EXIT_OK
