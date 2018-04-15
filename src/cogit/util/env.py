# -*- coding: utf-8 -*-
# pylint: disable=bad-continuation
""" OS utility functions
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

import io
import os

from cogit import constants


def create_cogit_gitignore_file(gitignore_path):
    """Creates .gitignore file at path specified (usually in COGIT_DIR_NAME).

    :param gitignore_path: The path to the .gitignore file to create if it
                           doesn't yet exist.
    :type gitignore_path: string
    """
    if not os.path.exists(gitignore_path):
        with io.open(gitignore_path, "wt") as out_file:
            out_file.write(u".repo/")
            out_file.write(u"overrides.d/")


def create_cogit_default_file(default_path):
    """Creates default.cfg file at path specified (usually in COGIT_DIR_NAME).

    :param default_path: The path to the default.cfg file to create if it
                         doesn't yet exist.
    :type default_path: string
    """
    if not os.path.exists(default_path):
        with io.open(default_path, "wt") as out_file:
            out_file.write(u"")


def create_cogit_dir_and_files(path=None):
    """Creates COGIT_DIR_NAME and COGIT_DIR_FILES at the path specified.

    :param path: The path to create COGIT_DIR_NAME and COGIT_DIR_FILES if
                 they don't exist. The default is None which means in the
                 current working directory.
    :type path: string or None
    """
    root_path = get_absolute_or_current_path(path)
    if not os.path.exists(root_path):
        os.mkdir(root_path)

    cogit_path = os.path.join(root_path, constants.COGIT_DIR_NAME)
    if not os.path.exists(cogit_path):
        os.mkdir(cogit_path)

    global_config = constants.COGIT_GLOBAL_CONFIG
    create_cogit_global_config(global_config)

    gitignore_path = os.path.join(cogit_path, ".gitignore")
    create_cogit_gitignore_file(gitignore_path)

    default_path = os.path.join(cogit_path, "default.cfg")
    create_cogit_default_file(default_path)


def create_cogit_global_config(config_path):
    """Creates cogit.cfg file at path specified (usually in COGIT_USER_DIR).

    :param config_path: The path to the cogit.cfg file to create if it
                        doesn't yet exist.
    :type config_path: string
    """
    config_dir = os.path.dirname(config_path)
    if not os.path.exists(config_dir):
        os.mkdir(config_dir)
    if not os.path.exists(config_path):
        with io.open(config_path, "wt") as out_file:
            out_file.write(u"")


def get_absolute_or_current_path(path):
    """Return absolute version of path specified or current working directory.

    :param path: The path to get absolute path to. The default is None which
                 means return absolute path to the current working directory.
    :type path: string or None

    :return: Returns the absolute version of path specified or current
             working directory.
    :rtype: Absolute path
    """
    if path is None:
        result = os.path.abspath(os.getcwd())
    else:
        result = os.path.abspath(path)
    return result


def get_cogit_root_and_current(path=None):
    """Walks from path specified searching for first and last COGIT_DIR_NAME
    directories found.

    :param path: The starting path to search from. The default is None which
                 means search from the current working directory.
    :type path: string or None

    :return: Returns the root and current CoGit paths found from the path
             specified. A cogit path is the path that contains a
             COGIT_DIR_NAME sub-directory and is used as the starting point
             for relative paths mentioned in CoGit configuration files.
    :rtype: Tuple containing the absolute paths to the root and current
            CoGit paths found.
    """
    first_found = None
    last_found = None
    current_path = get_absolute_or_current_path(path)
    next_path = os.path.dirname(current_path)
    while not next_path == current_path:
        test_path = os.path.join(current_path, constants.COGIT_DIR_NAME)
        if os.path.isdir(test_path):
            if first_found is None:
                first_found = current_path
            last_found = current_path
        current_path = next_path
        next_path = os.path.dirname(current_path)
    return last_found, first_found
