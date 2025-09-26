from .chunkedregion import *
from .coord import *
from .region import *

module_version = "1.0.0"
module_name = "tstructs"
module_description = "Tile map data structures for 2D and 3D worlds."

def check_module_version(version_expecting:str) -> bool:
    """
    Check if the current module version matches the expected version.

    :param version_expecting: The version string to check against (e.g., "1.0.0").
    :type version_expecting: str
    :return: True if the versions match, False otherwise.
    :rtype: bool
    """
    return module_version == version_expecting

def get_module_info() -> dict:
    """
    Get information about the module.

    :return: A dictionary containing the module's name, version, and description.
    :rtype: dict
    """
    return {
        "name": module_name,
        "version": module_version,
        "description": module_description
    }

