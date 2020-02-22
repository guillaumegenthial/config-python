"""Assembler"""

from typing import Dict

from cerberus import Validator

from libnn.vocab import Vocab
from libnn.layers import TimesTwoLayer, PlusOneLayer
from libnn.model import Model


class ModelAssembler:
    """Creates Model from dictionary"""

    # For Cerberus
    SCHEMA = {
        "vocab": {
            "type": "list", "nullable": True, "default": None,
        },
        "layers": {
            "type": "list",
            "schema": {
                "type": "dict",
                "schema": {
                    "layer_type": {
                        "type": "string", "nullable": False,
                    },
                    "layer_name": {
                        "type": "string", "nullable": False
                    }
                }
            },
            "nullable": False
        }
    }

    @staticmethod
    def from_dict(data: Dict) -> Model:
        """Build Model from dict

        Parameters
        ----------
        data : Dict
            Serialized Dictionary

        Returns
        -------
        Model
        """
        # Validate data using cerberus
        schema = Validator(ModelAssembler.SCHEMA)
        data = schema.normalized(data)
        if not schema.validate(data):
            raise ValueError(schema.errors)

        # Create vocab
        vocab = Vocab(data["vocab"])

        # Create layers
        layers = []
        for layer_data in data["layers"]:
            layer_type = layer_data["layer_type"]
            layer_name = layer_data["layer_name"]
            if layer_type == "TimesTwoLayer":
                layer = TimesTwoLayer(layer_name, vocab)
            elif layer_type == "PlusOneLayer":
                layer = PlusOneLayer(layer_name, vocab)
            else:
                raise ValueError(f"{layer_type} not recognized.")
            layers.append(layer)
        return Model(layers)
