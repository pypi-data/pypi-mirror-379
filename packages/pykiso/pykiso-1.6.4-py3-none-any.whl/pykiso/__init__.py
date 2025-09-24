##########################################################################
# Copyright (c) 2010-2022 Robert Bosch GmbH
# This program and the accompanying materials are made available under the
# terms of the Eclipse Public License 2.0 which is available at
# http://www.eclipse.org/legal/epl-2.0.
#
# SPDX-License-Identifier: EPL-2.0
##########################################################################

"""
pykiso - extensible framework for (embedded) integration testing.
*****************************************************************

:module: pykiso

:synopsis: ``pykiso`` is an extensible framework for (embedded) integration testing.

.. currentmodule:: pykiso

"""

try:
    from importlib import metadata
except ImportError:  # for Python<3.8
    import importlib_metadata as metadata

# get version from package metadata to automatically set the version dunder
__version__ = metadata.version(__name__)

from . import cli, config_parser, connector, logging_initializer, message, types
from .auxiliary import AuxiliaryInterface
from .connector import CChannel, Flasher
from .exceptions import AuxiliaryCreationError, InvalidTestModuleName, PykisoError, TestCollectionError
from .interfaces.dt_auxiliary import DTAuxiliaryInterface
from .logging_initializer import disable_logging
from .message import Message
from .test_coordinator import test_case, test_message_handler, test_suite
from .test_coordinator.test_case import BasicTest, RemoteTest, define_test_parameters, retry_test_case, xray
from .test_coordinator.test_execution import abort
from .test_coordinator.test_suite import (
    BasicTestSuiteSetup,
    BasicTestSuiteTeardown,
    RemoteTestSuiteSetup,
    RemoteTestSuiteTeardown,
)

logging_initializer.add_internal_log_levels()

# Experimental - load configuration and create auxiliaries
from .config_parser import parse_config
from .test_setup.config_registry import ConfigRegistry


def load_config(config_file: str):
    """Enable any user to load a pykiso yaml file from any script

    :param config_file: path to the pykiso yaml file

    """
    cfg = parse_config(config_file)
    ConfigRegistry.register_aux_con(cfg)
