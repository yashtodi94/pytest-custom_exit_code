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
        try:
            # Before pytest 5 the values were contants
            from _pytest.main import EXIT_NOTESTSCOLLECTED, EXIT_OK
            no_tests_collected = EXIT_NOTESTSCOLLECTED
            ok = EXIT_OK
        except ImportError:
            # From pytest 5 on the values are inside an enum
            from _pytest.main import ExitCode
            no_tests_collected = ExitCode.NO_TESTS_COLLECTED
            ok = ExitCode.OK

        if exitstatus == no_tests_collected:
            session.exitstatus = ok
