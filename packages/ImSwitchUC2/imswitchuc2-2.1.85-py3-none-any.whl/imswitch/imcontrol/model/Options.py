import os
from dataclasses import dataclass, field

from dataclasses_json import dataclass_json, Undefined, CatchAll

from imswitch.imcommon.model import dirtools
from imswitch import DEFAULT_DATA_PATH

@dataclass(frozen=False)
class RecordingOptions:
    if DEFAULT_DATA_PATH is None:
        outputFolder: str = os.path.join(dirtools.UserFileDirs.Root, 'recordings')
    else:
        outputFolder: str = os.path.join(DEFAULT_DATA_PATH, 'recordings')
    includeDateInOutputFolder: bool = True


@dataclass(frozen=False)
class WatcherOptions:
    outputFolder: str = os.path.join(dirtools.UserFileDirs.Root, 'scripts')


@dataclass_json(undefined=Undefined.INCLUDE)
@dataclass(frozen=False)
class Options:
    setupFileName: str  # JSON file that contains setup info
    recording: RecordingOptions = field(default_factory=RecordingOptions)
    watcher: WatcherOptions = field(default_factory=WatcherOptions)
    _catchAll: CatchAll = None



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
