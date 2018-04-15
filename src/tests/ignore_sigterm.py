# -*- coding: utf-8 -*-
# pylint: disable=bad-continuation
""" Catches and ignores SIGTERM signals for testing util.ext.execute_iter
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
import time


def ignore_sigterm_handler(signum, frame):
    # pylint: disable=unused-argument
    """Ignores all incoming signals.
    :param signum: The signal number caught.
    :type signum: int

    :param frame: The current stack frame when the signal occurred.
    :type frame: None or frame object
    """

    print("Signal {} ignored".format(signum))


signal.signal(signal.SIGTERM, ignore_sigterm_handler)


def main():
    """Infinite loop for using in Popen execute_iter tests.
    """
    print("Waiting indefinitely")
    while True:
        time.sleep(1)


if __name__ == "__main__":
    main()
