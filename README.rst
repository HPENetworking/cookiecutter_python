=====================
cookiecutter-template
=====================

About
=====

Cookiecutter template for a Python package.

See https://github.com/audreyr/cookiecutter.

- Open Source license: Apache 2.0.
- Automation setup using Tox_ for Python 2.7 and Python 3.4.
- Testing setup with pytest_.

  - Generates execution and coverage XML reports.
  - Autodiscovery and execution of doctest_.

- PEP8 compliance checking with Flake8_.

  - Includes a git pre-commit hook.
  - Includes configuration using EditorConfig_.

- Documentation setup with Sphinx_.

  - Automatic API generation using ``autosummary_generate``.
    Just list new modules in ``doc/reference.rst``.
  - Built-in support for PlantUML_ diagrams.


Usage
=====

Generate a new Python project using this template:

::

   pip install cookiecutter
   cookiecutter git@magma-git.austin.hp.com:testing/cookiecutter-template.git


Improvements
============

- Setup Travis CI and Tox integration.
- Setup Coveralls and Tox integration.
- Integrate documentation with http://shields.io/
- Add support for changelog generation using gitchangelog


.. _Tox: https://testrun.org/tox/
.. _pytest: http://pytest.org/
.. _doctest: https://docs.python.org/3/library/doctest.html
.. _Flake8: https://flake8.readthedocs.org/
.. _EditorConfig: http://editorconfig.org/
.. _Sphinx: http://sphinx-doc.org/
.. _PlantUML: http://plantuml.com/
