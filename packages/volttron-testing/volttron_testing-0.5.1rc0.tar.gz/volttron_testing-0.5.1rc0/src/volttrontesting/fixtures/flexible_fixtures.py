# -*- coding: utf-8 -*- {{{
# ===----------------------------------------------------------------------===
#
#                 Installable Component of Eclipse VOLTTRON
#
# ===----------------------------------------------------------------------===
#
# Copyright 2022 Battelle Memorial Institute
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not
# use this file except in compliance with the License. You may obtain a copy
# of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
#
# ===----------------------------------------------------------------------===
# }}}

"""
Pytest fixtures for flexible testing with mock or real message buses.

These fixtures allow tests to work with either mock or real VOLTTRON
instances based on configuration.
"""

import pytest
import os
from typing import Optional

from volttrontesting.testing_context import TestingContext
from volttrontesting.messagebus_factory import TestingConfig, MessageBusType


def pytest_addoption(parser):
    """Add command line options for test configuration"""
    parser.addoption(
        "--bus-type",
        action="store",
        default="mock",
        choices=["mock", "zmq", "rmq"],
        help="Message bus type to use for testing (default: mock)"
    )
    parser.addoption(
        "--volttron-home",
        action="store",
        default=None,
        help="VOLTTRON_HOME directory (for real bus testing)"
    )
    parser.addoption(
        "--bus-address",
        action="store",
        default="tcp://127.0.0.1:22916",
        help="Message bus address (for real bus testing)"
    )


@pytest.fixture(scope="session")
def testing_config(request) -> TestingConfig:
    """
    Create testing configuration from command line options or environment.
    
    Priority order:
    1. Command line arguments
    2. Environment variables
    3. Default values
    """
    # Check command line arguments first
    bus_type_str = request.config.getoption("--bus-type", default=None)
    volttron_home = request.config.getoption("--volttron-home", default=None)
    bus_address = request.config.getoption("--bus-address", default=None)
    
    # Fall back to environment variables
    if not bus_type_str:
        bus_type_str = os.environ.get("VOLTTRON_TEST_BUS", "mock")
    if not volttron_home:
        volttron_home = os.environ.get("VOLTTRON_HOME")
    if not bus_address:
        bus_address = os.environ.get("VOLTTRON_TEST_BUS_ADDRESS", "tcp://127.0.0.1:22916")
    
    # Map string to enum
    type_map = {
        "mock": MessageBusType.MOCK,
        "zmq": MessageBusType.ZMQ,
        "rmq": MessageBusType.RMQ
    }
    bus_type = type_map.get(bus_type_str.lower(), MessageBusType.MOCK)
    
    # Build configuration
    config = TestingConfig(
        bus_type=bus_type,
        volttron_home=volttron_home,
        instance_name=os.environ.get("VOLTTRON_INSTANCE_NAME", "test-instance")
    )
    
    if bus_type != MessageBusType.MOCK:
        config.bus_config = {
            "address": bus_address,
            "serverkey": os.environ.get("VOLTTRON_TEST_SERVERKEY", "")
        }
    
    return config


@pytest.fixture(scope="function")
def testing_context(testing_config) -> TestingContext:
    """
    Create a testing context for a single test.
    
    This fixture provides a clean testing environment for each test.
    """
    context = TestingContext(testing_config)
    context.setup()
    yield context
    context.teardown()


@pytest.fixture(scope="module")
def module_testing_context(testing_config) -> TestingContext:
    """
    Create a testing context shared across a test module.
    
    This fixture provides a testing environment that persists
    across all tests in a module.
    """
    context = TestingContext(testing_config)
    context.setup()
    yield context
    context.teardown()


@pytest.fixture
def mock_only(testing_context):
    """
    Skip test if not using mock message bus.
    
    Use this fixture for tests that only work with mock.
    """
    if not testing_context.is_mock_mode:
        pytest.skip("Test requires mock message bus")
    return testing_context


@pytest.fixture
def real_only(testing_context):
    """
    Skip test if not using real message bus.
    
    Use this fixture for tests that only work with real bus.
    """
    if testing_context.is_mock_mode:
        pytest.skip("Test requires real message bus")
    return testing_context


@pytest.fixture
def test_agent(testing_context):
    """
    Create a test agent for the test.
    
    The agent is automatically cleaned up after the test.
    """
    agent = testing_context.create_agent("test_agent")
    yield agent
    # Cleanup handled by testing_context


@pytest.fixture
def publisher_agent(testing_context):
    """Create a publisher agent for testing"""
    return testing_context.create_agent("publisher")


@pytest.fixture
def subscriber_agent(testing_context):
    """Create a subscriber agent for testing"""
    return testing_context.create_agent("subscriber")


# Markers for conditional test execution
def pytest_configure(config):
    """Register custom markers"""
    config.addinivalue_line(
        "markers", "mock_only: mark test to run only with mock message bus"
    )
    config.addinivalue_line(
        "markers", "real_only: mark test to run only with real message bus"
    )
    config.addinivalue_line(
        "markers", "all_buses: mark test to run with all message bus types"
    )


def pytest_runtest_setup(item):
    """Skip tests based on markers and configuration"""
    # Get the testing config from the item's session
    config = item.config.getoption("--bus-type", default="mock")
    is_mock = config == "mock"
    
    # Check for mock_only marker
    if item.get_closest_marker("mock_only") and not is_mock:
        pytest.skip("Test requires mock message bus")
    
    # Check for real_only marker
    if item.get_closest_marker("real_only") and is_mock:
        pytest.skip("Test requires real message bus")