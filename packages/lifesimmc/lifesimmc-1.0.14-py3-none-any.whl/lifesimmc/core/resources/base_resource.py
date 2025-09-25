from dataclasses import dataclass


@dataclass
class BaseResource:
    """Class representation of the base resource.

    Parameters
    ----------
    name : str
        The name of the resource.
    """
    name: str
