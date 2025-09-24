from imswitch import IS_HEADLESS
import warnings

if not IS_HEADLESS:
    from .AlignAverageWidget import AlignAverageWidget
    from .AlignmentLineWidget import AlignmentLineWidget
    from .AlignXYWidget import AlignXYWidget
    from .AutofocusWidget import AutofocusWidget
    from .basewidgets import WidgetFactory
    from .BeadRecWidget import BeadRecWidget
    from .ConsoleWidget import ConsoleWidget
    from .EtSTEDWidget import EtSTEDWidget
    from .FFTWidget import FFTWidget
    from .HoloWidget import HoloWidget
    from .JoystickWidget import JoystickWidget
    from .HistogrammWidget import HistogrammWidget
    from .STORMReconWidget import STORMReconWidget
    from .HoliSheetWidget import HoliSheetWidget
    from .FlowStopWidget import FlowStopWidget

    from .ObjectiveWidget import ObjectiveWidget
    from .TemperatureWidget import TemperatureWidget
    from .LEDMatrixWidget import LEDMatrixWidget
    from .WellPlateWidget import WellPlateWidget
    from .FocusLockWidget import FocusLockWidget
    from .FOVLockWidget import FOVLockWidget
    from .ImageWidget import ImageWidget
    from .LaserWidget import LaserWidget
    from .MotCorrWidget import MotCorrWidget
    from .LEDWidget import LEDWidget
    from .PositionerWidget import PositionerWidget
    from .StandaPositionerWidget import StandaPositionerWidget
    from .StandaStageWidget import StandaStageWidget
    from .RecordingWidget import RecordingWidget
    from .SLMWidget import SLMWidget
    from .ScanWidgetBase import ScanWidgetBase
    from .ScanWidgetMoNaLISA import ScanWidgetMoNaLISA
    from .ScanWidgetPointScan import ScanWidgetPointScan
    from .RotationScanWidget import RotationScanWidget
    from .RotatorWidget import RotatorWidget
    from .UC2ConfigWidget import UC2ConfigWidget
    from .SIMWidget import SIMWidget
    from .DPCWidget import DPCWidget
    from .MCTWidget import MCTWidget
    from .LepmonWidget import LepmonWidget
    from .ExperimentWidget import ExperimentWidget
    from .TimelapseWidget import TimelapseWidget
    from .ROIScanWidget import ROIScanWidget
    from .LightsheetWidget import LightsheetWidget
    from .WebRTCWidget import WebRTCWidget
    from .MockXXWidget import MockXXWidget
    from .JetsonNanoWidget import JetsonNanoWidget
    from .HistoScanWidget import HistoScanWidget
    from .WorkflowWidget import WorkflowWidget
    from .FlatfieldWidget import FlatfieldWidget
    from .PixelCalibrationWidget import PixelCalibrationWidget
    from .SquidStageScanWidget import SquidStageScanWidget
    from .ISMWidget import ISMWidget
    from .SettingsWidget import SettingsWidget
    from .SLMWidget import SLMWidget
    from .TilingWidget import TilingWidget
    from .basewidgets import WidgetFactory
    from .ULensesWidget import ULensesWidget
    from .ViewWidget import ViewWidget
    from .WatcherWidget import WatcherWidget
    try:
        from .HyphaWidget import HyphaWidget
    except ModuleNotFoundError:
        warnings.warn("HyphaWidget not available; please install imjoy-rpc module")
