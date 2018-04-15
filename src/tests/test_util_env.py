# *- coding: utf-8 -*-
# pylint: disable=wildcard-import, missing-docstring, no-self-use, bad-continuation
# pylint: disable=invalid-name, redefined-outer-name, too-few-public-methods
# pylint: disable=broad-except
""" Test env module in util package.
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
import shutil
import tempfile
from cogit import constants
from cogit.util import env


def make_tmp_cogit_dir(path=None):
    if path is None:
        temp_dir = tempfile.mkdtemp()
    else:
        temp_dir = path
        os.mkdir(temp_dir)
    temp_cogit_dir = os.path.join(temp_dir, constants.COGIT_DIR_NAME)
    os.mkdir(temp_cogit_dir)
    return temp_dir


def test_cogit_gitignore_file_is_created():
    temp_dir = tempfile.mkdtemp()
    gitignore_path = os.path.join(temp_dir, ".gitignore")
    env.create_cogit_gitignore_file(gitignore_path)
    assert os.path.exists(gitignore_path), "The .gitignore file wasn't created"
    shutil.rmtree(temp_dir)


def test_cogit_gitignore_file_already_exists():
    temp_dir = tempfile.mkdtemp()
    gitignore_path = os.path.join(temp_dir, ".gitignore")
    with io.open(gitignore_path, "wt") as out_file:
        out_file.write(u"some_bogus_content/")
    assert os.path.exists(gitignore_path), "The .gitignore wasn't created"
    env.create_cogit_gitignore_file(gitignore_path)
    with io.open(gitignore_path, "rt") as in_file:
        if not any(u"some_bogus_content/" == line.rstrip('\r\n') for line in in_file):
            assert False, "The .gitignore file was overwritten"
    shutil.rmtree(temp_dir)


def test_cogit_default_file_is_created():
    temp_dir = tempfile.mkdtemp()
    default_path = os.path.join(temp_dir, "default.cfg")
    env.create_cogit_default_file(default_path)
    assert os.path.exists(default_path), "The default.cfg file wasn't created"
    shutil.rmtree(temp_dir)


def test_cogit_default_file_already_exists():
    temp_dir = tempfile.mkdtemp()
    default_path = os.path.join(temp_dir, "default.cfg")
    with io.open(default_path, "wt") as out_file:
        out_file.write(u"some_bogus_content/")
    assert os.path.exists(default_path), "The default.cfg wasn't created"
    env.create_cogit_default_file(default_path)
    with io.open(default_path, "rt") as in_file:
        if not any(u"some_bogus_content/" == line.rstrip('\r\n')
                   for line in in_file):
            assert False, "The default.cfg file was overwritten"
    shutil.rmtree(temp_dir)


def test_cogit_dir_and_files_are_created_at_non_existing_path_specified():
    temp_dir = tempfile.mkdtemp()
    root_dir = os.path.join(temp_dir, "some_subdir")
    cogit_dir = os.path.join(root_dir, constants.COGIT_DIR_NAME)
    gitignore_path = os.path.join(cogit_dir, ".gitignore")
    default_path = os.path.join(cogit_dir, "default.cfg")
    global_config = os.path.join(temp_dir, constants.COGIT_CONFIG_NAME)
    constants.COGIT_GLOBAL_CONFIG = global_config
    env.create_cogit_dir_and_files(root_dir)
    assert os.path.isdir(root_dir), "The {} directory wasn't created".format(
        root_dir)
    assert os.path.isdir(cogit_dir), "The {} directory wasn't created".format(
        constants.COGIT_DIR_NAME)
    assert os.path.exists(gitignore_path), "The .gitignore file wasn't created"
    assert os.path.exists(global_config), "The global config file wasn't created"
    assert os.path.exists(default_path), "The default.cfg file wasn't created"
    shutil.rmtree(temp_dir)


def test_cogit_dir_and_files_are_created_in_working_directory():
    previous_working_path = os.getcwd()
    temp_dir = tempfile.mkdtemp()
    os.chdir(temp_dir)
    cogit_dir = os.path.join(temp_dir, constants.COGIT_DIR_NAME)
    gitignore_path = os.path.join(cogit_dir, ".gitignore")
    default_path = os.path.join(cogit_dir, "default.cfg")
    env.create_cogit_dir_and_files()
    os.chdir(previous_working_path)
    assert os.path.isdir(cogit_dir), "The {} directory wasn't created".format(
        constants.COGIT_DIR_NAME)
    assert os.path.exists(gitignore_path), "The .gitignore file wasn't created"
    assert os.path.exists(default_path), "The default.cfg file wasn't created"
    shutil.rmtree(temp_dir)


def test_cogit_dir_exists_but_files_are_missing():
    temp_dir = tempfile.mkdtemp()
    cogit_dir = os.path.join(temp_dir, constants.COGIT_DIR_NAME)
    os.mkdir(cogit_dir)
    gitignore_path = os.path.join(cogit_dir, ".gitignore")
    default_path = os.path.join(cogit_dir, "default.cfg")
    env.create_cogit_dir_and_files(temp_dir)
    assert os.path.isdir(cogit_dir), "The {} directory doesn't exist".format(
        constants.COGIT_DIR_NAME)
    assert os.path.exists(gitignore_path), "The .gitignore file wasn't created"
    assert os.path.exists(default_path), "The default.cfg file wasn't created"
    shutil.rmtree(temp_dir)


def test_get_cogit_root_and_current_for_bogus_path_returns_none():
    results = env.get_cogit_root_and_current("/some/bogus/path")
    assert results[0] is None, "No root cogit path was found"
    assert results[1] is None, "No current cogit path was found"


def test_get_cogit_root_and_current_with_no_path_provided_uses_cwd():
    previous_working_path = os.getcwd()
    temp_dir = make_tmp_cogit_dir()
    os.chdir(temp_dir)
    results = env.get_cogit_root_and_current()
    os.chdir(previous_working_path)
    shutil.rmtree(temp_dir)
    assert results[0] == results[1], "The root cogit path and current cogit path should be the same"
    assert results[0] == temp_dir, "The root cogit path should be the same as temp_dir"
    assert results[1] == temp_dir, "The current cogit path should be the same as temp_dir"


def test_get_cogit_root_and_current_for_single_level_cogit_returns_same():
    temp_dir = make_tmp_cogit_dir()
    results = env.get_cogit_root_and_current(temp_dir)
    shutil.rmtree(temp_dir)
    assert results[0] == results[1], "The root cogit path and current cogit path should be the same"
    assert results[0] == temp_dir, "The root cogit path should be the same as temp_dir"
    assert results[1] == temp_dir, "The current cogit path should be the same as temp_dir"


def test_get_cogit_root_and_current_for_multi_level_cogit_is_different():
    temp_dir = make_tmp_cogit_dir()
    second_dir = make_tmp_cogit_dir(os.path.join(temp_dir, "second"))
    results = env.get_cogit_root_and_current(second_dir)
    shutil.rmtree(temp_dir)
    assert results[0] != results[1], "The root cogit path and current cogit path should NOT be the same"
    assert results[0] == temp_dir, "The root cogit path should be the same as temp_dir"
    assert results[1] == second_dir, "The current cogit path should be the same as second_dir"
