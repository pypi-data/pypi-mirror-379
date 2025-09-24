import enum
import glob
import cv2
import os

import numpy as np
from PIL import Image

from imswitch.imcommon.framework import Signal, SignalInterface
from imswitch.imcommon.model import initLogger


class ROIScanManager(SignalInterface):

    def __init__(self, mctInfo, *args, **kwargs):
        self.sigROIScanMaskUpdated = Signal(object)  # (maskCombined)  # (maskCombined)
        super().__init__(*args, **kwargs)
        self.__logger = initLogger(self)

        if mctInfo is None:
            return

        self.update()

    def update(self):
        return None

# Copyright (C) 2020-2024 ImSwitch developers
# This file is part of ImSwitch.
#
# ImSwitch is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# ImSwitch is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.