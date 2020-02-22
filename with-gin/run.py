# pylint: disable=no-value-for-parameter
"""Generic Entry Point of the library"""

import gin

from libnn.model import Model


if __name__ == "__main__":
    gin.parse_config_file("config.gin")
    model = Model()  # Argument `layers` provided by gin
    print(model)
    print(model.forward(2))
