===================
cookiecutter_python
===================

About
=====

HPE Python project repository template for Open Source Software.

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

  - Automatic API generation using AutoAPI_.
  - Built-in support for PlantUML_, Graphviz_ and Ditaa_ diagrams using
    Plantweb_.

- Lightweight Python source distribution for PyPI.


Usage
=====

This repository has two branches:

- ``module``
- ``executable``

Which branch to use depends on the kind of project you want to create.
If an executable and a module is needed the use the ``executable`` branch.
If just a pure Python module is required then use the ``module`` branch.

Generate a new Python project using this template:

::

   pip3 install cookiecutter
   git clone https://github.com/HPENetworking/cookiecutter_python.git
   cd cookiecutter_python
   git checkout <executable or module>
   cookiecutter .


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
.. _AutoAPI: http://autoapi.readthedocs.org/
.. _PlantUML: http://plantuml.com/
.. _Graphviz: http://www.graphviz.org/
.. _Ditaa: http://ditaa.sourceforge.net/
.. _Plantweb: https://plantweb.readthedocs.io/
