# Allen Institute's plugin to upload coregisterd data
# This plugin should work with the config files in configs/coregistered/ folder
from __future__ import absolute_import
import six
from PIL import Image
import numpy as np
import os

from .path import PathProcessor
from .tile import TileProcessor


class AiPathProcessor(PathProcessor):
    def setup(self, parameters):
        """Set the params - for this just store where the file is located

        MUST HAVE THE CUSTOM PARAMETERS: "root_dir": "<path_to_tiles>"

        Args:
            parameters (dict): Parameters for the dataset to be processed

        Returns:
            None
        """
        self.parameters = parameters

    def process(self, x_index, y_index, z_index, t_index=None):

        filename = "{}/{}/{}.{}".format(z_index - 1, y_index, x_index, self.parameters["filetype"]) # using 'z_index - 1' because Nuno created the dataset starting at 0 

        return os.path.join(self.parameters["root_dir"], filename)


class AiTileProcessor(TileProcessor):
    """A Tile processor for a file where a multi-page TIFF contains all time points for a single z-slice"""
    def __init__(self):
        """Constructor to add custom class var"""
        TileProcessor.__init__(self)
        self.data = None

    def setup(self, parameters):
        """ Method to load the file for uploading - a very naive approach

        MUST HAVE THE CUSTOM PARAMETER: "datatype": "<uint8|uint16>"

        Args:
            parameters (dict): Parameters for the dataset to be processed

        Returns:
            None
        """
        self.parameters = parameters

    def process(self, file_path, x_index, y_index, z_index, t_index=0):

        return open(file_path, 'rb')
