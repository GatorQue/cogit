# -*- coding: utf-8 -*-
# pylint: disable=bad-continuation
""" Git utility functions
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
from cogit.util import ext


def git_clone(repository, directory=None, separate_git_dir=None, template_dir=None, environment=None):
    """Performs git clone with provided options.

    :param repository: The repository to clone.
    :type repository: url

    :param directory: The directory to perform the git clone command in.
    :type directory: path

    :param separate_git_dir: The separate git directory to store .git folder
                             contents in.
    :type separate_git_dir: path

    :param template_dir: The directory to use as template (e.g. hook and
                         ignore files).
    :type template_dir: path

    :param environment: The environment dictionary to use for the git clone
                        command.
    :type environment: dict

    :return: Returns the stdout output from the command executed.
    :rtype: List of strings produced by the Popen.communicate call used.
    """
    clone_cmd = ["git", "clone"]
    if separate_git_dir:
        clone_cmd.append("--separate-git-dir")
        clone_cmd.append(separate_git_dir)
    if template_dir:
        clone_cmd.append("--template={}".format(template_dir))
    clone_cmd.append("--")
    clone_cmd.append(repository)
    if directory:
        clone_cmd.append(directory)

    return ext.execute(clone_cmd, environment=environment)


def git_init(directory=None, separate_git_dir=None, template_dir=None, environment=None):
    """Performs git init with provided options.

    :param directory: The directory to perform the git init command in.
    :type directory: path

    :param separate_git_dir: The separate git directory to store .git folder
                             contents in.
    :type separate_git_dir: path

    :param template_dir: The directory to use as template (e.g. hook and
                         ignore files).
    :type template_dir: path

    :param environment: The environment dictionary to use for the git init
                        command.
    :type environment: dict

    :return: Returns the stdout output from the command executed.
    :rtype: List of strings produced by the Popen.communicate call used.
    """
    init_cmd = ["git", "init"]
    if separate_git_dir:
        init_cmd.append("--separate-git-dir")
        init_cmd.append(separate_git_dir)
    if template_dir:
        init_cmd.append("--template={}".format(template_dir))
    if directory:
        init_cmd.append(directory)

    return ext.execute(init_cmd, environment=environment)
