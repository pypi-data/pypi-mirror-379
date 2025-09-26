"""Docker integration package for Celestical.

Exports core helpers:
- Image: utilities to save/compress Docker images
- DockerMachine: high-level client for local Docker interactions
"""
from .image import Image
from .docker import DockerMachine
