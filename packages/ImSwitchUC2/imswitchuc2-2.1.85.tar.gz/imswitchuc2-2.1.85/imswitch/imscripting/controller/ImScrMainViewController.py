from .ConsoleController import ConsoleController
try:
    from PyQt5 import Qsci
    from .EditorController import EditorController
    isQsciAvailable = True
except:
    isQsciAvailable = False

from .FilesController import FilesController
from .OutputController import OutputController
from .basecontrollers import ImScrWidgetController
from imswitch import IS_HEADLESS

class ImScrMainViewController(ImScrWidgetController):
    """ Connected to ImScrMainView. """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not isQsciAvailable or IS_HEADLESS:
            return

        self.filesController = self._factory.createController(FilesController,
                                                              self._widget.files)

        self.editorController = self._factory.createController(EditorController,
                                                               self._widget.editor)
        self.consoleController = self._factory.createController(ConsoleController,
                                                                self._widget.console)
        self.outputController = self._factory.createController(OutputController,
                                                               self._widget.output)

        # Connect signals
        self._widget.sigNewFile.connect(self._commChannel.sigNewFile)
        self._widget.sigOpenFile.connect(self._commChannel.sigOpenFile)
        self._widget.sigSaveFile.connect(self._commChannel.sigSaveFile)
        self._widget.sigSaveAsFile.connect(self._commChannel.sigSaveAsFile)


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
