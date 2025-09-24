import importlib.util
import logging
import os
import time
from typing import Any, Callable

from imswitch.imcommon.framework import Signal, FrameworkUtils
from imswitch.imcommon.model import APIExport, generateAPI, initLogger


class _Actions:
    """ Additional functions intended to be made available through the
    scripting API. """

    def __init__(self, scriptScope, scriptPath=None):
        self._scriptScope = scriptScope
        self._scriptPath = scriptPath
        self._scriptLogger = initLogger('script')

    @APIExport()
    def importScript(self, path: str) -> Any:
        """ Imports the script at the specified path (either absolute or
        relative to the main script) and returns it as a module variable. """

        # Convert to absolute path
        if self._scriptPath is not None:
            path = os.path.join(os.path.dirname(self._scriptPath), path)

        # Load module
        spec = importlib.util.spec_from_file_location(os.path.basename(path), path)
        script = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(script)

        # Set script/actions scope
        script.__dict__.update(self._scriptScope)
        script.__dict__.update(getActionsScope(self._scriptScope, self._scriptPath))

        # Return
        return script

    @APIExport()
    def getScriptDirPath(self) -> str:
        """ Returns the path to the directory containing the running script.
        """
        return os.path.dirname(self._scriptPath)

    @APIExport()
    def getLogger(self) -> logging.LoggerAdapter:
        """ Returns a logger instance that can be used to print formatted
        messages to the console. """
        return self._scriptLogger

    @APIExport()
    def getWaitForSignal(self, signal: Signal,
                         pollIntervalSeconds: float = 1.0) -> Callable[[], None]:
        """ Returns a function that will wait for the specified signal to emit.
        The returned function will continuously check whether the signal has
        been emitted since its creation. The polling interval defaults to one
        second, and can be customized. """

        emitted = False

        def setEmitted():
            nonlocal emitted
            emitted = True

        signal.connect(setEmitted)

        def wait():
            while not emitted:
                FrameworkUtils.processPendingEventsCurrThread()
                time.sleep(pollIntervalSeconds)

            signal.disconnect(setEmitted)

        return wait


def getActionsScope(otherScope, scriptPath=None):
    """ Returns the script scope for the actions. """
    return generateAPI([_Actions(otherScope, scriptPath)])._asdict()


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
