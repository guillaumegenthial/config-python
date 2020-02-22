"""Generic Entry Point of the library"""

from pathlib import Path
import json

from libnn.assembler import ModelAssembler


if __name__ == "__main__":
    with Path("config.json").open() as file:
        model = ModelAssembler.from_dict(json.load(file))

    print(model)
    print(model.forward(2))
