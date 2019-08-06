# -*- coding: utf-8 -*-


def test_bar_fixture(testdir):
    """Make sure that pytest accepts our fixture."""

    # create a temporary pytest test module
    testdir.makepyfile("""""")

    # run pytest with the following cmd args
    result = testdir.runpytest(
        '--suppress-no-test-exit-code',
        '-v'
    )

    # make sure that that we get a '0' exit code for the testsuite
    assert result.ret == 0


def test_tests_failed(testdir):
    """Make sure that pytest accepts our fixture."""

    # create a temporary pytest test module
    testdir.makepyfile("""
        import pytest
        def test_fail():
            assert 1 == 2
        """)

    # run pytest with the following cmd args
    result = testdir.runpytest(
        '--suppress-tests-failed-exit-code',
        '-v'
    )

    # make sure that that we get a '0' exit code for the testsuite
    assert result.ret == 0
