..  cogit documentation master file

    Copyright ©  2017 Ryan Lindeman <ryanlindeman+cogit@gmail.com>

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


=============================================================================
Welcome to the “CoGit” manual!
=============================================================================

.. image:: _static/img/logo.png

*CoGit* is a Python library and command line tool that offers Multi-Git
repository and project management.


Important Links
---------------

  * `GitHub Project <https://github.com/GatorQue/cogit>`_
  * `Issue Tracker <https://github.com/GatorQue/cogit/issues>`_
  * `PyPI <https://pypi.python.org/pypi/rudiments/>`_
  * `Latest Documentation <https://cogit.readthedocs.org/en/latest/>`_


Installing
----------

*CoGit* can be installed from PyPI via ``pip install cogit`` as usual, see
`releases <https://github.com/GatorQue/cogit/releases>`_ on GitHub for an
overview of available versions – the project uses `semantic versioning
<http://semver.org/>`_ and follows `PEP 440
<https://www.python.org/dev/peps/pep-0440/>`_ conventions.

To get a bleeding-edge version from source, use these commands:

.. code-block:: shell

    repo="GatorQue/cogit"
    pip install -r "https://raw.githubusercontent.com/$repo/master/requirements.txt"
    pip install -UI -e "git+https://github.com/$repo.git#egg=${repo#*/}"

See the following section on how to create a full development environment.

To add bash completion, read the
`Click docs <http://click.pocoo.org/4/bashcomplete/#activation>`_
about it, or just follow these instructions:

.. code-block:: shell

    cmdname=cogit
    mkdir -p ~/.bash_completion.d
    ( export _$(tr a-z- A-Z_ <<<"$cmdname")_COMPLETE=source ; \
      $cmdname >~/.bash_completion.d/$cmdname.sh )
    grep /.bash_completion.d/$cmdname.sh ~/.bash_completion >/dev/null \
        || echo >>~/.bash_completion ". ~/.bash_completion.d/$cmdname.sh"
    . "/etc/bash_completion"


Contributing
------------

To create a working directory for this project, call these commands:

.. code-block:: shell

    git clone "https://github.com/GatorQue/cogit.git"
    cd "cogit"
    . .env --yes --develop
    invoke build --docs test check

Contributing to this project is easy, and reporting an issue or
adding to the documentation also improves things for every user.
You don’t need to be a developer to contribute.
See :doc:`CONTRIBUTING` for more.


Documentation Contents
----------------------

.. toctree::
    :maxdepth: 4

    usage
    api-reference
    CONTRIBUTING
    LICENSE


References
----------

Tools
^^^^^

-  `Cookiecutter <https://cookiecutter.readthedocs.io/en/latest/>`_
-  `PyInvoke <http://www.pyinvoke.org/>`_
-  `pytest <http://pytest.org/latest/contents.html>`_
-  `tox <https://tox.readthedocs.io/en/latest/>`_
-  `Pylint <http://docs.pylint.org/>`_
-  `twine <https://github.com/pypa/twine#twine>`_
-  `bpython <http://docs.bpython-interpreter.org/>`_
-  `yolk3k <https://github.com/myint/yolk#yolk>`_

Packages
^^^^^^^^

-  `Rituals <https://jhermann.github.io/rituals>`_
-  `Click <http://click.pocoo.org/>`_


Indices and Tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
