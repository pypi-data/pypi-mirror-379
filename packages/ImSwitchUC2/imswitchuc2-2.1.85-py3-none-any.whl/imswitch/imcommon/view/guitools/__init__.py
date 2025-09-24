from imswitch import IS_HEADLESS
if not IS_HEADLESS:
    # FIXME: hacky way to do that I guess..
    from .BetterPushButton import BetterPushButton
    from .joystick import Joystick
    from .BetterSlider import BetterSlider
    from .CheckableComboBox import CheckableComboBox
    from .FloatSlider import FloatSlider
    from .dialogtools import askYesNoQuestion, askForFilePath, askForFolderPath, askForTextInput, informationDisplay
    from .imagetools import bestLevels, minmaxLevels
    from .stylesheet import getBaseStyleSheet
    from .texttools import ordinalSuffix
    from .FileWatcher import FileWatcher
