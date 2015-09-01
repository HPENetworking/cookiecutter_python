.. toctree::

===============
Developer Guide
===============


Setup Development Environment
=============================

#. Install `pip` and `virtualenv`:

   ::

      sudo apt-get install python-pip
      sudo pip install virtualenv

#. Create a virtual environment:

   ::

      virtualenv {{ cookiecutter.repo_name }}_env
      source {{ cookiecutter.repo_name }}_env/bin/activate

#. Install application requirements and development requirements:

   ::

      cd {{ cookiecutter.repo_name }}
      pip install -r requirements.txt
      pip install -r requirements.dev.txt

#. Configure git pre-commit hook:

   ::

      flake8 --install-hook
      git config flake8.strict true


Building Documentation
======================

::

   tox -e doc

Output will be available at `.tox/doc/tmp/html`. It is recommended to install
the `webdev` package:

::

   sudo pip install webdev

So a development web server can serve any location like this:

::

   $ webdev .tox/doc/tmp/html
