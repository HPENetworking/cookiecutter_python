#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) {{ cookiecutter.year }} {{ cookiecutter.author }} <{{ cookiecutter.email }}>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

"""
Argument management module.
"""

from __future__ import unicode_literals, absolute_import
from __future__ import print_function, division

import logging
from argparse import ArgumentParser

from . import __version__


log = logging.get_logger(__name__)


FORMAT = '%(asctime)s:::%(levelname)s:::%(message)s'
V_LEVELS = {
    0: logging.ERROR,
    1: logging.WARNING,
    2: logging.INFO,
    3: logging.DEBUG,
}


def verify_args(args):
    """
    Verify that arguments are valid.
    """
    level = V_LEVELS.get(args.verbose, logging.DEBUG)
    logging.basicConfig(format=FORMAT, level=level)

    log.debug('Raw arguments:\n{}'.format(args))

    return args


def parse_args(argv=None):
    """
    Argument parsing routine.

    :para
    """
    parser = ArgumentParser(
        description='{{ cookiecutter.short_description }}'
    )
    parser.add_argument(
        '-v', '--verbose',
        help='Increase verbosity level',
        default=0,
        action='count'
    )
    parser.add_argument(
        '--version',
        action='version',
        version='{{ cookiecutter.project_name }} v{}'.format(__version__)
    )

    args = parser.parse_args(argv)
    args = verify_args(args)
    return args


__all__ = ['parse_args']
