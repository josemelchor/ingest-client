# Allen Institute's plugin to upload 2Photon Anatomical data
# This plugin should work with the config files in configs/2photon/ folder
from __future__ import absolute_import
# import six
# from PIL import Image
# import numpy as np
import os

from .path import PathProcessor
from .tile import TileProcessor


class AiPathProcessor(PathProcessor):
    def setup(self, parameters):
        self.parameters = parameters

    def process(self, x_index, y_index, z_index, t_index=None):

        filename = "{}{}.{}".format("2Photon_anatomical_cell_z", ("%04d" % z_index), self.parameters["filetype"])

        return os.path.join(self.parameters["root_dir"], filename)


class AiTileProcessor(TileProcessor):
    def __init__(self):
        TileProcessor.__init__(self)
        self.data = None

    def setup(self, parameters):
        self.parameters = parameters

    def process(self, file_path, x_index, y_index, z_index, t_index=0):

        return open(file_path, 'rb')
