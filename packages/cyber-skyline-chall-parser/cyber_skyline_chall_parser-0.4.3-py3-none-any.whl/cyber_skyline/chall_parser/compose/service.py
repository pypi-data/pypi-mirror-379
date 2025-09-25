# Copyright 2025 Cyber Skyline

# Permission is hereby granted, free of charge, to any person obtaining a 
# copy of this software and associated documentation files (the “Software”), 
# to deal in the Software without restriction, including without limitation 
# the rights to use, copy, modify, merge, publish, distribute, sublicense, 
# and/or sell copies of the Software, and to permit persons to whom the 
# Software is furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included 
# in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL 
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING 
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS 
# IN THE SOFTWARE.
"""
Docker Compose Service Configuration for CTF Challenges

This module defines a simplified Service class that represents a Docker Compose service
specifically tailored for CTF challenge deployment. It focuses on the essential fields
needed for challenge infrastructure while ignoring complex orchestration features.
"""

from typing import Iterator, Literal, Any
from attrs import define, field
import attrs.validators as v
from cyber_skyline.chall_parser.template import Template
from cyber_skyline.chall_parser.compose.validators import is_ipv4

type CapAdd = Literal['NET_ADMIN', 'SYS_PTRACE']

@define
class ServiceNetwork:
    """Represents a network attachment for a service.
    """
    ipv4_address: str | None = field(default=None, validator=v.optional(is_ipv4))  # Static IPv4 address for the service on this network
    

@define
class Service:
    """Represents a Docker Compose service configuration for CTF challenges.
    
    This is a simplified version of the full Docker Compose service specification,
    focusing only on the fields that are relevant for CTF challenge deployment.
    The design prioritizes clarity and security over comprehensive Docker feature support.
    """
    
    # Required fields - every service must have these
    image: str = field(validator=v.instance_of(str))  # Docker image to run (e.g., "nginx:latest", "postgres:13")
    hostname: str = field(validator=v.instance_of(str))  # Hostname for the container (important for networking and DNS resolution)

    # Explicitly ignored fields - these are common Docker Compose features
    # that we support but ignore because they are not relevant in production
    build: Any = field(default=None)  # Build context - not needed for pre-built challenge images
    ports: Any = field(default=None)  # Any port mapping that occurs should be occurring within the infrastructure
    stdin_open: Any = field(default=None)  # Interactive mode - probably not needed for most challenges
    tty: Any = field(default=None)  # TTY allocation - probably not needed for most challenges

    # Potentially ignored fields - these might be useful but are currently unsupported
    # TODO: Evaluate if these should be supported based on challenge requirements
    logging: Any = field(default=None)  # Custom logging configuration - might be useful for debugging
    healthcheck: Any = field(default=None)  # Health checks - could be useful for service reliability
    develop: Any = field(default=None)  # Development-specific features - probably not needed in production

    # Core operational fields - these are essential for most services
    command: str | list[str] | None = field(default=None, validator=v.or_(
        v.optional(v.instance_of(str)),
        v.optional(v.deep_iterable(v.instance_of(str), v.instance_of(list))) # type: ignore
    ))  # Override the default command
                                           # Can be string (shell form) or list (exec form)
    entrypoint: str | list[str] | None = field(default=None)  # Override the default entrypoint

    # Environment and configuration
    environment: dict[str, Template | str] | list[str] | None = field(
        default=None)
    # Environment variables for the container
    # - dict form: {"VAR": "value"} or {"VAR": Template("fake.name()")}
    # - list form: ["VAR=value", "OTHER_VAR=other_value"]
    # Template support allows dynamic variable generation for each challenge instance
    
    # Networking configuration
    networks: list[str] | dict[str, ServiceNetwork | None] | None = field(default=None)
    # Network connections for the service
    # - list form: ["network1", "network2"] - simple network attachment
    # - dict form: {"network1": None} - allows for future network-specific configuration

    
    # Security and capabilities
    cap_add: list[CapAdd] | None = field(default=None)
    # Linux capabilities to add to the container
    # Limited to specific capabilities that might be needed for challenges:
    # - NET_ADMIN: For network-related challenges (packet capture, routing)
    # - SYS_PTRACE: For debugging/reverse engineering challenges
    
    # Resource constraints - important for preventing resource abuse
    mem_limit: int | str | None = field(default=None)  # Memory limit (e.g., "512m", "1g")
    memswap_limit: int | str | None = field(default=None)  # Memory + swap limit
    cpus: float | str | None = field(default=None)  # CPU limit (e.g., 0.5, "1.5")

    # User and permissions
    user: str | None = field(default=None)  # User to run the container as (e.g., "1000:1000", "nobody")
    # TODO: Decide on security policy for user specification
    # Should we enforce non-root users? Allow specific user patterns only?
    
    # Extension fields for custom docker extension configuration
    extensions: dict[str, Any] | None = field(default=None)
    # Custom fields starting with 'x-' for docker extension metadata
    # These are not part of the standard Docker Compose spec but can be useful
    # for custom docker extensions or metadata

    def warnings(self) -> Iterator[str]:
        if self.build:
            yield "build field is ignored in production"
        if self.ports:
            yield "ports field is ignored in production"
        if self.stdin_open:
            yield "stdin_open field is ignored in production"
        if self.tty:
            yield "tty field is ignored in production"
        if self.logging:
            yield "logging field is currently unsupported and will be ignored"
        if self.healthcheck:
            yield "healthcheck field is currently unsupported and will be ignored"
        if self.develop:
            yield "develop field is currently unsupported and will be ignored"

# Design Notes:
# 
# 1. Security Focus: Many Docker Compose features are intentionally excluded
#    to reduce attack surface and complexity. For example, volume mounts,
#    privileged mode, and host networking are not supported.
#
# 2. Template Integration: The environment field supports Template objects
#    to enable dynamic content generation using the Faker library.
#
# 3. Minimal but Extensible: The class includes only essential fields but
#    provides extension mechanisms for future expansion.
#
# 4. Type Safety: All fields are properly typed to enable static analysis
#    and better development experience.
#
# TODO: Evaluate if init process support is needed for proper signal handling
