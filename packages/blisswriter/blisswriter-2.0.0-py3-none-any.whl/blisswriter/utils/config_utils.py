"""Static Bliss configuration utilities
"""

import os


def static_config():
    """
    :returns bliss.config.static.Config:
    """
    from bliss.config import static  # avoid bliss patching on import

    return static.get_config()


def static_root(root=None):
    """
    :returns ConfigNode:
    """
    if root is None:
        return static_config().root
    else:
        return root


def beamline(root=None, default="id00"):
    """
    :returns str:
    """
    from bliss import current_session

    name = default
    for k in "BEAMLINENAME", "BEAMLINE":
        name = os.environ.get(k, name)
    root = static_root(root=root)
    name = root.get("beamline", name)
    name = current_session.scan_saving_config.get("beamline", name)
    return name.lower()


def institute(root=None, default=""):
    """
    :returns str:
    """
    root = static_root(root=root)
    name = default
    name = root.get("institute", name)
    name = root.get("laboratory", name)
    name = root.get("synchrotron", name)
    return name


def instrument(root=None, default=""):
    """
    :returns str:
    """
    root = static_root(root=root)
    default_instrument = institute(root=root, default=default)
    if default and default.lower() not in default_instrument.lower():
        default_instrument = f"{default_instrument}-{default}"
    name = root.get("instrument", default_instrument)
    return name
