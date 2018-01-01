# *- coding: utf-8 -*-
# pylint: disable=wildcard-import, unused-wildcard-import, missing-docstring
# pylint: disable=redefined-outer-name, no-self-use, bad-continuation
""" Test '__main__' CLI stub.

    See http://click.pocoo.org/3/testing/
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

#import os
import sys

import sh
import pytest
from click.testing import CliRunner

from markers import *
from cogit import __version__ as version
from cogit import __main__ as main
#from cogit import commands


UsageError = sh.ErrorReturnCode_2  # pylint: disable=no-member


@pytest.fixture
def cmd():
    """Command fixture."""
    return sh.Command(main.__app_name__)


@cli
@integration
def test_cli_help(cmd):
    result = cmd('--help')
    lines = result.stdout.decode('ascii').splitlines()

    assert main.__app_name__ in lines[0].split(), "Command name is reported"


@cli
@integration
def test_cli_version(cmd):
    result = cmd('--version')
    stdout = result.stdout.decode('ascii')
    reported_version = stdout.split()[1]
    py_version = sys.version.split()[0]

    assert version in stdout, "Version string contains version"
    assert reported_version[:len(version)] == version, "Version is 2nd field"
    assert py_version in stdout, "Python version is reported"


@cli
@integration
def test_cli_invalid_option(cmd):
    with pytest.raises(UsageError):
        cmd('--this-is-certainly-not-a-supported-option')


@cli
@integration
def test_cli_invalid_sub_command(cmd):
    with pytest.raises(UsageError):
        cmd.sub_command_that_does_not_exist()


@cli
def test_cmd_missing():
    runner = CliRunner()
    result = runner.invoke(main.cli)

    assert result.exit_code == 0


@cli
def test_cmd_help():
    runner = CliRunner()
    result = runner.invoke(main.cli, args=('help',))
    if result.exit_code:
        print(vars(result))
        print('~' * 78)
        print(result.output_bytes)
        print('~' * 78)
    #words = result.output.split()

    assert result.exit_code == 0
    #assert 'configuration' in words
    #assert any(i.endswith(os.sep + 'cli.conf') for i in words), \
    #       "Some '.conf' files listed in " + repr(words)
