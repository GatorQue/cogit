# *- coding: utf-8 -*-
# pylint: disable=wildcard-import, missing-docstring, no-self-use, bad-continuation
# pylint: disable=invalid-name, redefined-outer-name, too-few-public-methods
# pylint: disable=broad-except
""" Test git module in util package.
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
import tempfile
import shutil
from cogit.util import git


def create_init_dir(temp_dir):
    init_dir = os.path.join(temp_dir, "init_dir")
    git.git_init(directory=init_dir)
    return init_dir


def test_git_clone_repository():
    previous_working_path = os.getcwd()
    temp_dir = tempfile.mkdtemp()
    init_dir = create_init_dir(temp_dir)
    clone_dir = os.path.join(temp_dir, "clone_dir")
    os.mkdir(clone_dir)
    git_dir = os.path.join(clone_dir, "init_dir", ".git")
    os.chdir(clone_dir)
    output = git.git_clone(init_dir)
    os.chdir(previous_working_path)
    assert os.path.isdir(git_dir), "The {} directory wasn't created".format(
        git_dir)
    assert output is not None, "The git clone command output was empty"
    shutil.rmtree(temp_dir)


def test_git_clone_separate_git_dir():
    previous_working_path = os.getcwd()
    temp_dir = tempfile.mkdtemp()
    init_dir = create_init_dir(temp_dir)
    separate_dir = os.path.join(temp_dir, "separate_dir")
    clone_dir = os.path.join(temp_dir, "clone_dir")
    os.mkdir(clone_dir)
    git_file = os.path.join(clone_dir, "init_dir", ".git")
    os.chdir(clone_dir)
    output = git.git_clone(init_dir, separate_git_dir=separate_dir)
    os.chdir(previous_working_path)
    assert os.path.isdir(separate_dir), "The {} directory wasn't created".format(
        separate_dir)
    assert os.path.isfile(git_file), "The {} file wasn't created".format(
        git_file)
    assert output is not None, "The git clone command output was empty"
    shutil.rmtree(temp_dir)


def test_git_clone_template_dir():
    previous_working_path = os.getcwd()
    temp_dir = tempfile.mkdtemp()
    template_dir = os.path.join(temp_dir, "template_dir")
    os.mkdir(template_dir)
    description_file = os.path.join(template_dir, "description")
    with io.open(description_file, "wt") as description:
        description.write(u"My description file\n")
    init_dir = create_init_dir(temp_dir)
    clone_dir = os.path.join(temp_dir, "clone_dir")
    os.mkdir(clone_dir)
    git_dir = os.path.join(clone_dir, "init_dir", ".git")
    description_file_copy = os.path.join(git_dir, "description")
    os.chdir(clone_dir)
    output = git.git_clone(init_dir, template_dir=template_dir)
    os.chdir(previous_working_path)
    assert os.path.isdir(git_dir), "The {} directory wasn't created".format(
        git_dir)
    assert os.path.isfile(description_file_copy), "The {} file wasn't created".format(
        description_file_copy)
    assert output is not None, "The git clone command output was empty"
    shutil.rmtree(temp_dir)


def test_git_clone_directory():
    previous_working_path = os.getcwd()
    temp_dir = tempfile.mkdtemp()
    init_dir = create_init_dir(temp_dir)
    clone_dir = os.path.join(temp_dir, "clone_dir")
    git_dir = os.path.join(clone_dir, ".git")
    os.chdir(temp_dir)
    output = git.git_clone(init_dir, directory=clone_dir)
    os.chdir(previous_working_path)
    assert os.path.isdir(clone_dir), "The {} directory wasn't created".format(
        clone_dir)
    assert os.path.isdir(git_dir), "The {} directory wasn't created".format(
        git_dir)
    assert output is not None, "The git clone command output was empty"
    shutil.rmtree(temp_dir)


def test_git_clone_directory_and_separate_git_dir():
    previous_working_path = os.getcwd()
    temp_dir = tempfile.mkdtemp()
    separate_dir = os.path.join(temp_dir, "separate_dir")
    init_dir = create_init_dir(temp_dir)
    clone_dir = os.path.join(temp_dir, "clone_dir")
    git_file = os.path.join(clone_dir, ".git")
    os.chdir(temp_dir)
    output = git.git_clone(init_dir, directory=clone_dir, separate_git_dir=separate_dir)
    os.chdir(previous_working_path)
    assert os.path.isdir(clone_dir), "The {} directory wasn't created".format(
        clone_dir)
    assert os.path.isdir(separate_dir), "The {} directory wasn't created".format(
        separate_dir)
    assert os.path.isfile(git_file), "The {} file wasn't created".format(
        git_file)
    assert output is not None, "The git clone command output was empty"
    shutil.rmtree(temp_dir)


def test_git_init_no_args():
    previous_working_path = os.getcwd()
    temp_dir = tempfile.mkdtemp()
    git_dir = os.path.join(temp_dir, ".git")
    os.chdir(temp_dir)
    output = git.git_init()
    os.chdir(previous_working_path)
    assert os.path.isdir(git_dir), "The {} directory wasn't created".format(
        git_dir)
    assert output is not None, "The git init command output was empty"
    shutil.rmtree(temp_dir)


def test_git_init_separate_git_dir():
    previous_working_path = os.getcwd()
    temp_dir = tempfile.mkdtemp()
    separate_dir = os.path.join(temp_dir, "separate_dir")
    init_dir = os.path.join(temp_dir, "init_dir")
    git_file = os.path.join(init_dir, ".git")
    os.mkdir(init_dir)
    os.chdir(init_dir)
    output = git.git_init(separate_git_dir=separate_dir)
    os.chdir(previous_working_path)
    assert os.path.isdir(separate_dir), "The {} directory wasn't created".format(
        separate_dir)
    assert os.path.isfile(git_file), "The {} file wasn't created".format(
        git_file)
    assert output is not None, "The git init command output was empty"
    shutil.rmtree(temp_dir)


def test_git_init_template_dir():
    previous_working_path = os.getcwd()
    temp_dir = tempfile.mkdtemp()
    template_dir = os.path.join(temp_dir, "template_dir")
    os.mkdir(template_dir)
    description_file = os.path.join(template_dir, "description")
    with io.open(description_file, "wt") as description:
        description.write(u"My description file\n")
    init_dir = os.path.join(temp_dir, "init_dir")
    git_dir = os.path.join(init_dir, ".git")
    description_file_copy = os.path.join(git_dir, "description")
    os.mkdir(init_dir)
    os.chdir(init_dir)
    output = git.git_init(template_dir=template_dir)
    os.chdir(previous_working_path)
    assert os.path.isdir(git_dir), "The {} directory wasn't created".format(
        git_dir)
    assert os.path.isfile(description_file_copy), "The {} file wasn't created".format(
        description_file_copy)
    assert output is not None, "The git init command output was empty"
    shutil.rmtree(temp_dir)


def test_git_init_directory():
    previous_working_path = os.getcwd()
    temp_dir = tempfile.mkdtemp()
    init_dir = os.path.join(temp_dir, "init_dir")
    git_dir = os.path.join(init_dir, ".git")
    os.chdir(temp_dir)
    output = git.git_init(directory=init_dir)
    os.chdir(previous_working_path)
    assert os.path.isdir(init_dir), "The {} directory wasn't created".format(
        init_dir)
    assert os.path.isdir(git_dir), "The {} directory wasn't created".format(
        git_dir)
    assert output is not None, "The git init command output was empty"
    shutil.rmtree(temp_dir)


def test_git_init_directory_and_separate_git_dir():
    previous_working_path = os.getcwd()
    temp_dir = tempfile.mkdtemp()
    separate_dir = os.path.join(temp_dir, "separate_dir")
    init_dir = os.path.join(temp_dir, "init_dir")
    git_file = os.path.join(init_dir, ".git")
    os.chdir(temp_dir)
    output = git.git_init(directory=init_dir, separate_git_dir=separate_dir)
    os.chdir(previous_working_path)
    assert os.path.isdir(init_dir), "The {} directory wasn't created".format(
        init_dir)
    assert os.path.isdir(separate_dir), "The {} directory wasn't created".format(
        separate_dir)
    assert os.path.isfile(git_file), "The {} file wasn't created".format(
        git_file)
    assert output is not None, "The git init command output was empty"
    shutil.rmtree(temp_dir)
