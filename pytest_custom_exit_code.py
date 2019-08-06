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
    group.addoption(
        '--suppress-tests-failed-exit-code',
        action='store_true',
        default=False,
        help='Suppress the "some tests failed" exit code.'
    )


@pytest.hookimpl(trylast=True)
def pytest_sessionfinish(session, exitstatus):
    try:
        # Before pytest 5 the values were contants
        from _pytest.main import EXIT_NOTESTSCOLLECTED, EXIT_TESTSFAILED, EXIT_OK
        no_tests_collected = EXIT_NOTESTSCOLLECTED
        tests_failed = EXIT_TESTSFAILED
        ok = EXIT_OK
    except ImportError:
        # From pytest 5 on the values are inside an enum
        from pytest import ExitCode
        no_tests_collected = ExitCode.NO_TESTS_COLLECTED
        tests_failed = ExitCode.TESTS_FAILED
        ok = ExitCode.OK

    if session.config.getoption('--suppress-no-test-exit-code'):
        if exitstatus == no_tests_collected:
            session.exitstatus = ok

    if session.config.getoption('--suppress-tests-failed-exit-code'):
        if exitstatus == tests_failed:
            session.exitstatus = ok
