# -*- coding: utf-8 -*-
# pylint: disable=invalid-name
""" py.test markers.

    For details needed to understand these tests, refer to:
        https://pytest.org/
        http://pythontesting.net/start-here/
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
from __future__ import absolute_import, unicode_literals, print_function

import pytest


# See also setup.cfg » [pytest] » markers
cli = pytest.mark.cli
integration = pytest.mark.integration
online = pytest.mark.online


# Export all markers
__all__ = [_k
           for _k, _v in globals().items()
           if _v.__class__ is cli.__class__]
