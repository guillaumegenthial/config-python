"""Generic Entry Point of the library"""

from pathlib import Path
import json

from libnn.serializable import Serializable

if __name__ == "__main__":
    with Path("config.json").open() as file:
        model = Serializable.from_dict(json.load(file))

    print(model)
    print(model.forward(2))
