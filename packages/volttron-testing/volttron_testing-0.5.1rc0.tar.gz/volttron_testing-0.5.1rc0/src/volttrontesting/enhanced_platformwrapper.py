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
Enhanced PlatformWrapper that uses the factory pattern and manages package
installations with proper cleanup.
"""

from __future__ import annotations

import atexit
import logging
import os
import subprocess
import sys
import tempfile
from contextlib import contextmanager
from pathlib import Path
from typing import Optional, Dict, List, Any, Union
import json

from volttrontesting.platformwrapper import (
    PlatformWrapper as BasePlatformWrapper,
    create_volttron_home,
    with_os_environ
)
from volttrontesting.messagebus_factory import MessageBusType, TestingConfig

_log = logging.getLogger(__name__)


class PackageManager:
    """
    Manages package installation and cleanup for testing.
    
    Ensures that packages are properly installed for testing and
    always cleaned up, even if exceptions occur.
    """
    
    def __init__(self):
        self._installed_packages: List[str] = []
        self._original_packages: Dict[str, str] = {}
        self._cleanup_registered = False
        
    def _get_installed_version(self, package_name: str) -> Optional[str]:
        """Get the currently installed version of a package"""
        try:
            result = subprocess.run(
                [sys.executable, "-m", "pip", "show", package_name],
                capture_output=True,
                text=True,
                check=False
            )
            if result.returncode == 0:
                for line in result.stdout.split('\n'):
                    if line.startswith('Version:'):
                        return line.split(':', 1)[1].strip()
        except Exception as e:
            _log.debug(f"Could not get version for {package_name}: {e}")
        return None
    
    def _save_original_state(self, package_name: str):
        """Save the original state of a package before modifying it"""
        version = self._get_installed_version(package_name)
        if version:
            self._original_packages[package_name] = version
            _log.info(f"Saved original state: {package_name}=={version}")
    
    def install_package(self, package_spec: str, pre_release: bool = True):
        """
        Install a package for testing.
        
        :param package_spec: Package specification (e.g., 'volttron-lib-zmq')
        :param pre_release: Whether to allow pre-release versions
        """
        # Extract package name from spec
        package_name = package_spec.split('[')[0].split('==')[0].split('>=')[0]
        
        # Save original state before installing
        self._save_original_state(package_name)
        
        # Build pip command
        cmd = [sys.executable, "-m", "pip", "install"]
        if pre_release:
            cmd.append("--pre")
        cmd.append(package_spec)
        
        _log.info(f"Installing package: {package_spec}")
        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                check=True
            )
            self._installed_packages.append(package_name)
            _log.info(f"Successfully installed {package_spec}")
            
            # Register cleanup on first install
            if not self._cleanup_registered:
                atexit.register(self.cleanup_all)
                self._cleanup_registered = True
                
        except subprocess.CalledProcessError as e:
            _log.error(f"Failed to install {package_spec}: {e.stderr}")
            raise
    
    def uninstall_package(self, package_name: str):
        """Uninstall a package"""
        try:
            cmd = [sys.executable, "-m", "pip", "uninstall", "-y", package_name]
            subprocess.run(cmd, capture_output=True, text=True, check=True)
            _log.info(f"Uninstalled {package_name}")
        except subprocess.CalledProcessError as e:
            _log.warning(f"Failed to uninstall {package_name}: {e.stderr}")
    
    def restore_original_state(self, package_name: str):
        """Restore a package to its original state"""
        if package_name in self._original_packages:
            original_version = self._original_packages[package_name]
            _log.info(f"Restoring {package_name} to version {original_version}")
            try:
                cmd = [
                    sys.executable, "-m", "pip", "install",
                    f"{package_name}=={original_version}"
                ]
                subprocess.run(cmd, capture_output=True, text=True, check=True)
            except subprocess.CalledProcessError as e:
                _log.error(f"Failed to restore {package_name}: {e.stderr}")
    
    def cleanup_all(self):
        """
        Clean up all installed packages and restore original state.
        
        This is called automatically at exit or can be called manually.
        """
        _log.info("Cleaning up installed packages")
        
        # Uninstall packages that were installed for testing
        for package in self._installed_packages:
            if package not in self._original_packages:
                # Package wasn't installed before, remove it
                self.uninstall_package(package)
            else:
                # Package was installed before, restore original version
                self.restore_original_state(package)
        
        self._installed_packages.clear()
        self._original_packages.clear()
    
    def __enter__(self):
        """Context manager entry"""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit - ensures cleanup even on exception"""
        self.cleanup_all()
        return False


class EnhancedPlatformWrapper(BasePlatformWrapper):
    """
    Enhanced PlatformWrapper that integrates with the factory pattern
    and manages package installations.
    """
    
    def __init__(self, config: Optional[TestingConfig] = None, **kwargs):
        """
        Initialize enhanced platform wrapper.
        
        :param config: Testing configuration from factory
        :param kwargs: Additional arguments for base PlatformWrapper
        """
        self.config = config or TestingConfig.from_env()
        self.package_manager = PackageManager()
        
        # Determine message bus type
        messagebus = None
        if self.config.bus_type == MessageBusType.ZMQ:
            messagebus = "zmq"
        elif self.config.bus_type == MessageBusType.RMQ:
            messagebus = "rmq"
        
        # Initialize base class
        super().__init__(
            messagebus=messagebus,
            **kwargs
        )
        
        # Track installed messagebus packages
        self._messagebus_package = None
        
    def setup_messagebus_package(self):
        """
        Install the appropriate message bus package based on configuration.
        """
        if self.config.bus_type == MessageBusType.ZMQ:
            _log.info("Installing ZMQ message bus package")
            self.package_manager.install_package(
                "volttron-lib-zmq",
                pre_release=True
            )
            self._messagebus_package = "volttron-lib-zmq"
            
        elif self.config.bus_type == MessageBusType.RMQ:
            _log.info("Installing RabbitMQ message bus package")
            self.package_manager.install_package(
                "volttron-lib-rmq",
                pre_release=True
            )
            self._messagebus_package = "volttron-lib-rmq"
    
    def startup_platform(self, *args, **kwargs):
        """
        Start the platform with appropriate message bus setup.
        """
        # Install message bus package if needed
        if self.messagebus and not self._messagebus_package:
            self.setup_messagebus_package()
        
        # Call parent startup
        return super().startup_platform(*args, **kwargs)
    
    def shutdown_platform(self):
        """
        Shutdown platform and clean up packages.
        """
        try:
            super().shutdown_platform()
        finally:
            # Always clean up packages
            self.cleanup_packages()
    
    def cleanup_packages(self):
        """Clean up installed packages"""
        self.package_manager.cleanup_all()
    
    def install_test_agent(self, 
                           agent_package: str,
                           config: Optional[Union[dict, str]] = None,
                           start: bool = True,
                           pre_release: bool = True) -> str:
        """
        Install an agent package for testing.
        
        :param agent_package: Package name or path to install
        :param config: Agent configuration
        :param start: Whether to start the agent
        :param pre_release: Whether to allow pre-release versions
        :return: Agent UUID
        """
        # Install the agent package
        if not os.path.exists(agent_package):
            # It's a package name, install from PyPI
            self.package_manager.install_package(agent_package, pre_release)
        
        # Now install the agent using parent method
        return self.install_agent(
            agent_wheel=agent_package if os.path.exists(agent_package) else None,
            config_file=config,
            start=start
        )
    
    def __enter__(self):
        """Context manager entry"""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Context manager exit - ensures cleanup even on exception.
        """
        try:
            self.shutdown_platform()
        except Exception as e:
            _log.error(f"Error during platform shutdown: {e}")
        finally:
            # Always clean up packages
            self.cleanup_packages()
        return False


@contextmanager
def platform_wrapper_context(config: Optional[TestingConfig] = None, **kwargs):
    """
    Context manager for platform wrapper with automatic cleanup.
    
    Usage:
        with platform_wrapper_context() as wrapper:
            wrapper.startup_platform(...)
            # Run tests
        # Platform shutdown and package cleanup happens automatically
    
    :param config: Testing configuration
    :param kwargs: Additional arguments for PlatformWrapper
    :return: Platform wrapper instance
    """
    wrapper = EnhancedPlatformWrapper(config, **kwargs)
    try:
        yield wrapper
    finally:
        # Ensure cleanup even if exception occurs
        try:
            wrapper.shutdown_platform()
        except Exception as e:
            _log.error(f"Error during shutdown: {e}")
        finally:
            wrapper.cleanup_packages()


# Factory function to create appropriate wrapper based on config
def create_platform_wrapper(config: Optional[TestingConfig] = None, **kwargs):
    """
    Factory function to create a platform wrapper.
    
    :param config: Testing configuration
    :param kwargs: Additional arguments
    :return: Platform wrapper instance
    """
    if config is None:
        config = TestingConfig.from_env()
    
    if config.bus_type == MessageBusType.MOCK:
        # For mock, we don't need a real platform
        _log.info("Mock mode selected, no platform wrapper needed")
        return None
    
    # Create enhanced wrapper for real message buses
    return EnhancedPlatformWrapper(config, **kwargs)


if __name__ == "__main__":
    import logging
    logging.basicConfig(level=logging.INFO)
    
    # Example 1: Using context manager for automatic cleanup
    print("\n=== Example 1: Context Manager ===")
    config = TestingConfig(bus_type=MessageBusType.ZMQ)
    
    with platform_wrapper_context(config) as wrapper:
        print("Platform wrapper created")
        # wrapper.startup_platform(...)
        # Run tests
    print("Platform and packages cleaned up automatically")
    
    # Example 2: Manual cleanup with exception safety
    print("\n=== Example 2: Manual with Exception Safety ===")
    wrapper = EnhancedPlatformWrapper(config)
    try:
        wrapper.setup_messagebus_package()
        # wrapper.startup_platform(...)
        # Run tests
    finally:
        wrapper.cleanup_packages()
    print("Packages cleaned up even if exception occurred")
    
    # Example 3: Using with fixtures
    print("\n=== Example 3: Fixture Style ===")
    def platform_fixture():
        config = TestingConfig.from_env()
        wrapper = create_platform_wrapper(config)
        if wrapper:
            yield wrapper
            wrapper.cleanup_packages()
        else:
            yield None  # Mock mode
    
    print("Ready for use in pytest fixtures")