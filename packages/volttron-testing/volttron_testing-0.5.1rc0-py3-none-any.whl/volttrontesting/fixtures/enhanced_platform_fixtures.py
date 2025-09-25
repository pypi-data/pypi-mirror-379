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
Enhanced platform fixtures that automatically manage message bus packages.

Simply import this instead of volttron_platform_fixtures to get automatic
package management.
"""

import pytest
import logging

# Import the enhancement FIRST - this automatically patches PlatformWrapper
# This MUST happen before any imports that use PlatformWrapper
import volttrontesting.platformwrapper_enhanced

# Now import the regular fixtures - they'll use the enhanced PlatformWrapper
from volttrontesting.fixtures.volttron_platform_fixtures import *

_log = logging.getLogger(__name__)

# The fixtures are now enhanced automatically!
_log.info("Platform fixtures enhanced with automatic package management")

# Optional: Add a fixture that explicitly uses the context manager
@pytest.fixture(scope="module")
def managed_volttron_instance():
    """
    Volttron instance fixture with explicit package management.
    
    This ensures packages are cleaned up even if tests fail.
    """
    from volttrontesting.platformwrapper_enhanced import managed_platform_wrapper
    
    with managed_platform_wrapper(messagebus="zmq") as wrapper:
        # Setup the platform
        wrapper.startup_platform(
            vip_address="tcp://127.0.0.1:22916",
            auth_dict={},
            encrypt=False
        )
        
        yield wrapper
        
        # Cleanup happens automatically via context manager
    
    _log.info("Platform and packages cleaned up")