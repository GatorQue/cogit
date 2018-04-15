# -*- coding: utf-8 -*-
# pylint: disable=bad-continuation
""" External utility functions
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
import signal
import subprocess
import time


def execute(command, environment=None):
    """Executes command and verifies returncode == 0 and returns stdout.

    :param command: The command or list of command arguments to execute using
                    the Popen command.
    :type command: string or list

    :param environment: The environment dictionary to use for the Popen
                        command.
    :type environment: dict

    :return: Returns the stdout output from the command executed.
    :rtype: List of strings produced by the Popen.communicate call used.
    """
    return subprocess.check_output(command,
                                   env=environment,
                                   stderr=subprocess.STDOUT,
                                   universal_newlines=True)


def execute_iter(command, environment=None, terminate_timeout=10):
    """Executes command and yields stdout/stderr as a generator method.

    :param command: The command or list of command arguments to execute using
                    the Popen command.
    :type command: string or list

    :param environment: The environment dictionary to use for the Popen
                        command.
    :type environment: dict

    :param terminate_timeout: The time in seconds to wait before calling
                              Popen.terminate and Popen.kill if process is
                              still running when generator method is
                              interrupted or raises GenerateExit error on
                              garbage collection.
    :type terminate_timeout: int or float
    """
    popen = subprocess.Popen(command,
                             env=environment,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.STDOUT,
                             bufsize=1,
                             universal_newlines=True)
    try:
        output = []
        for stdout_line in iter(popen.stdout.readline, ""):
            print(stdout_line)
            output.append(stdout_line)
            yield stdout_line
    except (GeneratorExit, KeyboardInterrupt):
        if popen.poll() is None:
            popen.terminate()
        end_time = time.time() + terminate_timeout
        while popen.poll() is None and time.time() < end_time:
            time.sleep(0.1)
    else:
        popen.wait()
    finally:
        popen.stdout.close()
        if popen.poll() is None:
            popen.kill()
        end_time = time.time() + terminate_timeout
        while popen.poll() is None:
            if time.time() >= end_time:  # pragma: no cover
                popen.returncode = -signal.SIGKILL
                break
            time.sleep(0.1)
        if popen.returncode:
            raise subprocess.CalledProcessError(popen.returncode,
                                                command,
                                                output)
