from abc import ABC, abstractmethod
from typing import Union


class LEDMatrixManager(ABC):
    """ Abstract base class for managers that control LEDMatrixs. Each type of
    LEDMatrix corresponds to a manager derived from this class. """

    @abstractmethod
    def __init__(self, LEDMatrixInfo, name: str, isBinary: bool, valueUnits: str,
                 valueDecimals: int, isModulated: bool = False) -> None:
        """
        Args:
            LEDMatrixInfo:
        """

        self._LEDMatrixInfo = LEDMatrixInfo
        self.__name = name
        self.__pattern = None
        self.valueUnits = valueUnits
        self.valueDecimals = valueDecimals
        self.isModulated = isModulated
        self.isBinary = False
        self.wavelength = 0
        self.valueRangeMin = 0
        self.valueRangeMax = 255
        self.valueRangeStep = 1
        self.valueUnits = ""
        self.__currentState = None


    def name(self) -> str:
        """ Unique LEDMatrix name, defined in the LEDMatrix's setup info. """
        return self.__name

    def setEnabled(self, enabled: bool) -> None:
        """ Sets whether the LEDMatrix is enabled. """
        pass

    def setAll(self, intensity=0, getReturn=True) -> None:
        """ Sets the value of the LEDMatrix. """
        pass

    def setPattern(self, pattern) -> None:
        """ Sets the value of the LEDMatrix. """
        pass

    def setEnabled(self, enabled) -> None:
        """ Sets the value of the LEDMatrix. """
        pass

    def setLEDSingle(self, index=0, intensity=0) -> None:
        """ Sets the value of the LEDMatrix. """
        pass

    def setIndividualPattern(self, pattern, getReturn=False) -> None:
        """ Sets the value of the LEDMatrix. """
        pass

    def setEnabled(self, enabled) -> None:
        """ Sets the value of the LEDMatrix. """
        pass

    def setValue(self, value) -> None:
        """ Sets the value of the LEDMatrix. """
        pass

    def getState(self) -> Union[None, str]:
        """ Returns the state of the LEDMatrix. """
        return self.__currentState

    def setState(self, state) -> None:
        """ Sets the state of the LEDMatrix. """

    def setRing(self, radius: int, intensity: int) -> None:
        """ Sets the value of the LEDMatrix. """
        pass

    def setCircle(self, radius: int, intensity: int) -> None:
        """ Sets the value of the LEDMatrix. """
        pass

    def setHalves(self, intensity: int, region: str) -> None:
        """ Sets the value of the LEDMatrix. """
        pass

    def setStatus(self, status:str="idle") -> None:
        """ Sets the value of the LEDMatrix (e.g. for error indication). """
        pass


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
