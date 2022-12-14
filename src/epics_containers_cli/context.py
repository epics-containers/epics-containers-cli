"""
Define a context for passing root parameters to sub-commands
"""

from dataclasses import dataclass


@dataclass
class Context:
    beamline: str = ""
    helm_registry: str = ""
    image_registry: str = ""
    show_cmd: bool = False
