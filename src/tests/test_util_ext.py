# *- coding: utf-8 -*-
# pylint: disable=wildcard-import, missing-docstring, no-self-use, bad-continuation
# pylint: disable=invalid-name, redefined-outer-name, too-few-public-methods
# pylint: disable=broad-except
""" Test ext module in util package.
"""
# Copyright ©  2017 Ryan Lindeman <ryanlindeman+cogit@gmail.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
from __future__ import absolute_import, print_function

import os
import subprocess
import time
from cogit.util import ext


def test_execute_raises_on_non_zero_return_code():
    try:
        ext.execute("/bin/false")
        assert False, "Expecting CalledProcessError to be raised by execute"
    except subprocess.CalledProcessError as err:
        assert 0 != err.returncode, "Invalid return code returned in error"
        assert "/bin/false" in err.cmd, "Invalid command returned in error"
        assert [] != err.output, "Invalid output returned in error"


def test_execute_returns_on_zero_return_code():
    try:
        ext.execute_iter("/bin/true")
    except Exception:
        assert False, "Expecting no error to be raised by execute"


def test_execute_returns_command_output():
    echo_cmd = ["/bin/echo", "Hi mom,\nI'm home!"]
    try:
        output = ext.execute(echo_cmd)
        assert [] != output, "Invalid output returned by execute"
    except Exception:
        assert False, "Expecting no error to be raised by execute"


def test_execute_iter_raises_on_non_zero_return_code():
    try:
        for _ in ext.execute_iter("/bin/false"):
            pass
        assert False, "Expecting CalledProcessError to be raised by execute_iter"
    except subprocess.CalledProcessError as err:
        assert 0 != err.returncode, "Invalid return code returned in error"
        assert "/bin/false" in err.cmd, "Invalid command returned in error"
        assert [] == err.output, "Invalid output returned in error"


def test_execute_iter_returns_on_zero_return_code():
    try:
        for _ in ext.execute_iter("/bin/true"):
            pass
    except Exception:
        assert False, "Expecting no error to be raised by execute_iter"


def test_execute_iter_yields_non_empty_lines():
    for line in ext.execute_iter("/usr/bin/env"):
        assert "" != line, "Expecting execute_iter to return non-empty lines"


def test_execute_iter_raises_stop_iteration_on_no_output():
    sleep_cmd = ["/bin/sleep", "1s"]
    gen = ext.execute_iter(sleep_cmd)
    try:
        gen.next()
    except StopIteration:
        pass
    else:
        assert False, "Expecting StopIteration to be raised by execute_iter"


def test_execute_iter_calls_process_kill_on_generator_close():
    ignore_sigterm_filepath = os.path.join(os.path.dirname(__file__),
                                           "ignore_sigterm.py")
    ignore_sigterm_cmd = ["python", "-u", ignore_sigterm_filepath]
    gen = ext.execute_iter(ignore_sigterm_cmd, terminate_timeout=0.5)
    try:
        gen.next()
        del gen
    except subprocess.CalledProcessError as err:
        assert 0 != err.returncode, "Invalid return code returned in error"
        assert "python" in err.cmd, "Invalid command returned in error"
        assert [] != err.output, "Invalid output returned in error"


def test_execute_iter_calls_process_terminate_on_generator_close():
    cat_cmd = ["/bin/cat", "/dev/kmsg"]
    gen = ext.execute_iter(cat_cmd)
    try:
        gen.next()
        del gen
    except subprocess.CalledProcessError as err:
        assert 0 != err.returncode, "Invalid return code returned in error"
        assert "/bin/cat" in err.cmd, "Invalid command returned in error"
        assert [] != err.output, "Invalid output returned in error"


def test_execute_iter_skips_calling_process_terminate_on_generator_close():
    echo_cmd = ["/bin/echo", "my mom\nhas fleas\n"]
    gen = ext.execute_iter(echo_cmd)
    try:
        gen.next()
        time.sleep(0.5)  # allow echo process to exit
        del gen
    except subprocess.CalledProcessError as err:
        assert 0 != err.returncode, "Invalid return code returned in error"
        assert "/usr/bin/env" in err.cmd, "Invalid command returned in error"
        assert [] != err.output, "Invalid output returned in error"
