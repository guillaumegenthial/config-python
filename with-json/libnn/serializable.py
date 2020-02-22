"""Base Class for Serializable Classes"""

from abc import ABC
from typing import Dict


class Serializable(ABC):
    """Base Class for Serializable Classes"""

    @classmethod
    def from_params(cls, params: Dict):
        """Create instance of cls from params dictionary"""

        def _is_serializable_dict(d):
            return isinstance(d, dict) and {"type", "params"} <= d.keys()

        # Reload possibly nested serializable definition
        for key, value in params.items():
            if _is_serializable_dict(value):
                params[key] = Serializable.from_dict(value)
            elif isinstance(value, list) and value:
                for idx, val in enumerate(value):
                    if _is_serializable_dict(val):
                        value[idx] = Serializable.from_dict(val)

        return cls(**params)

    @staticmethod
    def from_dict(data: Dict):
        cls = str_to_class(data["type"])
        return cls.from_params(data["params"])


def str_to_class(import_str: str):
    """Import class using import string"""
    parts = import_str.split(".")
    module = ".".join(parts[:-1])
    m = __import__(module)
    for comp in parts[1:]:
        m = getattr(m, comp)
    return m
