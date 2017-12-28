# cogit

Multi-Git repository and project management system.

 [![Travis CI](https://api.travis-ci.org/GatorQue/cogit.svg)](https://travis-ci.org/GatorQue/cogit)
 [![Coveralls](https://img.shields.io/coveralls/GatorQue/cogit.svg)](https://coveralls.io/r/GatorQue/cogit)
 [![GitHub Issues](https://img.shields.io/github/issues/GatorQue/cogit.svg)](https://github.com/GatorQue/cogit/issues)
 [![License](https://img.shields.io/pypi/l/cogit.svg)](https://github.com/GatorQue/cogit/blob/master/LICENSE)
 [![Development Status](https://pypip.in/status/cogit/badge.svg)](https://pypi.python.org/pypi/cogit/)
 [![Latest Version](https://img.shields.io/pypi/v/cogit.svg)](https://pypi.python.org/pypi/cogit/)
 [![Download format](https://pypip.in/format/cogit/badge.svg)](https://pypi.python.org/pypi/cogit/)
 [![Downloads](https://img.shields.io/pypi/dw/cogit.svg)](https://pypi.python.org/pypi/cogit/)

**Contents**

 * [Overview](#overview)
 * [Installation](#installation)
 * [Usage](#usage)
 * [Contributing](#contributing)
 * [Trouble-Shooting](#trouble-shooting)
 * [References](#references)
 * [Acknowledgements](#acknowledgements)


## Overview

**TODO**


## Installation

*CoGit* can be installed via ``pip install cogit`` as usual,
see [releases](https://github.com/GatorQue/cogit/releases) for an overview of available versions.
To get a bleeding-edge version from source, use these commands:

```sh
repo="GatorQue/cogit"
pip install -r "https://raw.githubusercontent.com/$repo/master/requirements.txt"
pip install -UI -e "git+https://github.com/$repo.git#egg=${repo#*/}"
```

See [Contributing](#contributing) on how to create a full development environment.

To add bash completion, read the [Click docs](http://click.pocoo.org/4/bashcomplete/#activation) about it,
or just follow these instructions:

```sh
cmdname=cogit
mkdir -p ~/.bash_completion.d
( export _$(tr a-z- A-Z_ <<<"$cmdname")_COMPLETE=source ; \
  $cmdname >~/.bash_completion.d/$cmdname.sh )
grep /.bash_completion.d/$cmdname.sh ~/.bash_completion >/dev/null \
    || echo >>~/.bash_completion ". ~/.bash_completion.d/$cmdname.sh"
. "/etc/bash_completion"
```


## Usage

…


## Contributing

Contributing to this project is easy, and reporting an issue or
adding to the documentation also improves things for every user.
You don’t need to be a developer to contribute.
See [CONTRIBUTING](https://github.com/GatorQue/cogit/blob/master/docs/CONTRIBUTING.rst) for more.

As a documentation author or developer,
to **create a working directory** for this project,
call these commands:

```sh
git clone "https://github.com/GatorQue/cogit.git"
cd "cogit"
command . .env --yes --develop  # add '--virtualenv /usr/bin/virtualenv' for Python2
invoke build --docs test check
```

For this to work, you might also need to follow some
[setup procedures](https://py-generic-project.readthedocs.io/en/latest/installing.html#quick-setup)
to make the necessary basic commands available on *Linux*, *Mac OS X*, and *Windows*.

**Running the test suite** can be done several ways, just call ``invoke test`` for a quick check.
Run ``invoke test.tox`` for testing with *all* supported Python versions
(if you [have them available](https://github.com/jhermann/priscilla/tree/master/pyenv)),
or be more selective by e.g. calling ``invoke test.tox -e py27,py34``.

Use ``invoke check`` to **run a code-quality scan**.

To **start a watchdog that auto-rebuilds documentation** and reloads the opened browser tab on any change,
call ``invoke docs -w -b`` (stop the watchdog using the ``-k`` option).


## Trouble-Shooting

### 'pkg-resources not found' or similar during virtualenv creation

If you get errors regarding ``pkg-resources`` during the virtualenv creation,
update your build machine's ``pip`` and ``virtualenv``.
The versions on many distros are just too old to handle current infrastructure (especially PyPI).

This is the one exception to “never sudo pip”, so go ahead and do this:

```sh
sudo pip install -U pip virtualenv
```


## References

**Tools**

* [Cookiecutter](http://cookiecutter.readthedocs.io/en/latest/)
* [PyInvoke](http://www.pyinvoke.org/)
* [pytest](http://pytest.org/latest/contents.html)
* [tox](https://tox.readthedocs.io/en/latest/)
* [Pylint](http://docs.pylint.org/)
* [twine](https://github.com/pypa/twine#twine)
* [bpython](http://docs.bpython-interpreter.org/)
* [yolk3k](https://github.com/myint/yolk#yolk)

**Packages**

* [Rituals](https://jhermann.github.io/rituals)
* [Click](http://click.pocoo.org/)


## Acknowledgements

…
