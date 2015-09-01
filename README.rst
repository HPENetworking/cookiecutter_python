=====================
cookiecutter-template
=====================

Cookiecutter template for a Python package.

See https://github.com/audreyr/cookiecutter.

- Open Source license: Apache 2.0.
- Automation setup using Tox_ for Python 2.7 and Python 3.4.
- Testing setup with pytest_.

  - Includes coverage report.
  - Autodiscovery and execution of doctest_.

- PEP8 compliance checking with Flake8_.

  - Includes a git pre-commit hook.
  - Includes configuration using EditorConfig_.

- Documentation setup with Sphinx_.


Usage
-----

Generate a new Python project using this template:

::

   pip install cookiecutter
   cookiecutter git@magma-git.austin.hp.com:testing/cookiecutter-template.git


.. _Tox: https://testrun.org/tox/
.. _pytest: http://pytest.org/
.. _doctest: https://docs.python.org/3/library/doctest.html
.. _Flake8: https://flake8.readthedocs.org/
.. _EditorConfig: http://editorconfig.org/
.. _Sphinx: http://sphinx-doc.org/
