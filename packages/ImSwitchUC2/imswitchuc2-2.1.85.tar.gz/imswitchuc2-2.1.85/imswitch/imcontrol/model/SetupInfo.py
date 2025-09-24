from dataclasses import dataclass, field, make_dataclass
from typing import Any, Dict, List, Optional, Union

from dataclasses_json import dataclass_json, Undefined, CatchAll


@dataclass(frozen=False)
class DeviceInfo:
    analogChannel: Optional[Union[str, int]]
    """ Channel for analog communication. ``null`` if the device is digital or
    doesn't use NI-DAQ. If an integer is specified, it will be translated to
    "Dev1/ao{analogChannel}". """

    digitalLine: Optional[Union[str, int]]
    """ Line for digital communication. ``null`` if the device is analog or
    doesn't use NI-DAQ. If an integer is specified, it will be translated to
    "Dev1/port0/line{digitalLine}". """

    managerName: str
    """ Manager class name. """

    managerProperties: Dict[str, Any]
    """ Properties to be read by the manager. """

    def getAnalogChannel(self):
        """ :meta private: """
        if isinstance(self.analogChannel, int):
            return f'Dev1/ao{self.analogChannel}'  # for backwards compatibility
        else:
            return self.analogChannel

    def getDigitalLine(self):
        """ :meta private: """
        if isinstance(self.digitalLine, int):
            return f'Dev1/port0/line{self.digitalLine}'  # for backwards compatibility
        else:
            return self.digitalLine


@dataclass(frozen=False)
class DetectorInfo(DeviceInfo):
    forAcquisition: bool = False
    """ Whether the detector is used for acquisition. """

    forFocusLock: bool = False
    """ Whether the detector is used for focus lock. """


@dataclass(frozen=False)
class LaserInfo(DeviceInfo):
    valueRangeMin: Optional[Union[int, float]]
    """ Minimum value of the laser. ``null`` if laser doesn't setting a value.
    """

    valueRangeMax: Optional[Union[int, float]]
    """ maximum value of the laser. ``null`` if laser doesn't setting a value.
    """

    wavelength: Union[int, float]
    """ Laser wavelength in nanometres. """

    freqRangeMin: Optional[int] = 0
    """ Minimum value of frequency modulation. Don't fill if laser doesn't support it. """

    freqRangeMax: Optional[int] = 0
    """ Minimum value of frequency modulation. Don't fill if laser doesn't support it. """

    freqRangeInit: Optional[int] = 0
    """ Initial value of frequency modulation. Don't fill if laser doesn't support it. """

    valueRangeStep: float = 1.0
    """ The default step size of the value range that the laser can be set to.
    """


@dataclass(frozen=False)
class LEDInfo(DeviceInfo):
    valueRangeMin: Optional[Union[int, float]]
    """ Minimum value of the laser. ``null`` if laser doesn't setting a value.
    """

    valueRangeMax: Optional[Union[int, float]]
    """ maximum value of the laser. ``null`` if laser doesn't setting a value.
    """

    valueRangeStep: float = 1.0
    """ The default step size of the value range that the laser can be set to.
    """


@dataclass(frozen=False)
class LEDMatrixInfo(DeviceInfo):
    pass


@dataclass(frozen=False)
class PositionerInfo(DeviceInfo):
    axes: List[str]
    """ A list of axes (names) that the positioner controls. """

    isPositiveDirection: bool = True
    """ Whether the direction of the positioner is positive. """

    forPositioning: bool = False
    """ Whether the positioner is used for manual positioning. """

    forScanning: bool = False
    """ Whether the positioner is used for scanning. """

    resetOnClose: bool = True
    """ Whether the positioner should be reset to 0-position upon closing ImSwitch. """

    stageOffsets: Dict[str, float] = field(default_factory=dict)
    """ Stage offsets available to select (map preset name -> stage name -> """

@dataclass(frozen=False)
class RS232Info:
    managerName: str
    """ RS232 manager class name. """

    managerProperties: Dict[str, Any]
    """ Properties to be read by the RS232 manager. """


@dataclass(frozen=False)
class SLMInfo:
    monitorIdx: int
    """ Index of the monitor in the system list of monitors (indexing starts at
    0). """

    width: int
    """ Width of SLM, in pixels. """

    height: int
    """ Height of SLM, in pixels. """

    wavelength: int
    """ Wavelength of the laser line used with the SLM. """

    pixelSize: float
    """ Pixel size or pixel pitch of the SLM, in millimetres. """

    angleMount: float
    """ The angle of incidence and reflection of the laser line that is shaped
    by the SLM, in radians. For adding a blazed grating to create off-axis
    holography. """

    correctionPatternsDir: str
    """ Directory of .bmp images provided by Hamamatsu for flatness correction
    at various wavelengths. A combination will be chosen based on the
    wavelength. """


@dataclass(frozen=False)
class UC2ConfigInfo:
    pass


@dataclass(frozen=False)
class SIMInfo:
    monitorIdx: int
    """ Index of the monitor in the system list of monitors (indexing starts at
    0). """

    width: int
    """ Width of SLM, in pixels. """

    height: int
    """ Height of SLM, in pixels. """

    wavelength: int
    """ Wavelength of the laser line used with the SLM. """

    pixelSize: float
    """ Pixel size or pixel pitch of the SLM, in millimetres. """

    angleMount: float = 0.0
    """ The angle of incidence and reflection of the laser line that is shaped
    by the SLM, in radians. For adding a blazed grating to create off-axis
    holography. """

    patternsDir: str = ""
    """ Directory of .bmp images provided by Hamamatsu for flatness correction
    at various wavelengths. A combination will be chosen based on the
    wavelength. """


    fastAPISIM_host: str = "192.168.xxx.xxx"

    fastAPISIM_port: str = "8000"

    isFastAPISIM: bool = False

    nRotations: int = 3

    nPhases: int = 3

    simMagnefication: float = 1.0

    isFastAPISIM: bool = False

    simPixelsize: float = 1.0

    simNA: float = 1.0

    simETA: float = 1.0

    simN: float = 1.0

    tWaitSequence: float = 0.0


@dataclass(frozen=False)
class DPCInfo:
    wavelength: int
    """ Wavelength of the laser line used with the SLM. """

    pixelsize: float
    """ Pixel size or pixel pitch of the SLM, in millimetres. """

    magnefication: float

    NA: float

    NAi: float

    n: float

    rotations: List[int]

@dataclass(frozen=False)
class ObjectiveInfo:
    pixelsizes: List
    NAs: List
    magnifications: List
    objectiveNames: List
    objectivePositions: List
    homeDirection: int = -1
    homePolarity: int = 1
    homeSpeed: int = 20000
    homeAcceleration: int = 20000
    calibrateOnStart: bool = True
    active: bool = True

@dataclass(frozen=False)
class MCTInfo:
    tWait: int

class ROIScanInfo:
    pass

@dataclass(frozen=False)
class LightsheetInfo:
    pass


@dataclass(frozen=False)
class WebRTCInfo:
    pass

@dataclass(frozen=False)
class HyphaInfo:
    pass

@dataclass(frozen=False)
class MockXXInfo:
    pass

@dataclass(frozen=False)
class JetsonNanoInfo:
    pass

@dataclass(frozen=False)
class HistoScanInfo:
    PreviewCamera: str = None
    pass

@dataclass(frozen=False)
class StresstestInfo:
    pass

@dataclass(frozen=False)
class WorkflowInfo:
    pass

@dataclass(frozen=False)
class FlowStopInfo:
    pass

@dataclass(frozen=False)
class LepmonInfo:
    pass

@dataclass(frozen=False)
class FlatfieldInfo:
    pass

@dataclass(frozen=False)
class PixelCalibrationInfo:
    pass


@dataclass(frozen=False)
class ExperimentInfo:
    """Configuration for experiment management, including OMERO integration."""
    
    # OMERO configuration
    omeroServerUrl: Optional[str] = "localhost"
    """ OMERO server URL. """
    
    omeroUsername: Optional[str] = ""
    """ OMERO username for authentication. """
    
    omeroPassword: Optional[str] = ""
    """ OMERO password for authentication. """
    
    omeroPort: Optional[int] = 4064
    """ OMERO server port. """
    
    omeroGroupId: Optional[int] = -1
    """ OMERO group ID for uploads. -1 for default group. """
    
    omeroProjectId: Optional[int] = -1
    """ OMERO project ID for uploads. -1 for no specific project. """
    
    omeroDatasetId: Optional[int] = -1
    """ OMERO dataset ID for uploads. -1 for no specific dataset. """
    
    omeroEnabled: bool = False
    """ Whether OMERO integration is enabled. """
    
    omeroConnectionTimeout: int = 30
    """ Connection timeout for OMERO in seconds. """
    
    omeroUploadTimeout: int = 300
    """ Upload timeout for OMERO in seconds. """


@dataclass(frozen=False)
class ISMInfo:
    wavelength: int
    """ Wavelength of the laser line used with the SLM. """

    angleMount: float
    """ The angle of incidence and reflection of the laser line that is shaped
    by the SLM, in radians. For adding a blazed grating to create off-axis
    holography. """

    patternsDir: str
    """ Directory of .bmp images provided by Hamamatsu for flatness correction
    at various wavelengths. A combination will be chosen based on the
    wavelength. """


@dataclass(frozen=False)
class FocusLockInfo:
    camera: str
    """ Detector name. """

    positioner: str
    """ Positioner name. """

    updateFreq: int
    """ Update frequency, in milliseconds. """

    cropCenter: list 
    """ Center point for cropping the camera image. """

    cropSize: int 
    """ Size of the cropped camera image. """

    piKp: float
    """ Default kp value of feedback loop. """

    piKi: float
    """ Default ki value of feedback loop. """
    
    focusLockMetric: str
    """ Method to use for focus lock. Options: 'astigmatism', 'phase', 'defocus'. """
    
    laserName: str
    """ Name of the laser to use for focus lock. """
    
    laserValue: int
    """ Value of the laser to use for focus lock. This is usually a wavelength in nm. """


@dataclass(frozen=False)
class ArkitektInfo:
    enabled: bool = True
    """ Whether Arkitekt integration is enabled. """

    appName: str = "imswitch"
    """ Application name for Arkitekt registration. """

    redeemToken: str = ""
    """ Redeem token for Arkitekt authentication. """

    url: str = "http://go.arkitekt.io"
    """ Arkitekt server URL. """

    syncInAsync: bool = True
    """ Enable sync-in-async mode for Koil. """

    deconvolveActionHash: str = "c58c90edbf6e208e3deafdd6f885553d6e027573f0ddc3b59ced3911f016ef4f"
    """ Hash of the deconvolution action in Arkitekt. """


@dataclass(frozen=False)
class FOVLockInfo:
    camera: str
    """ Detector name. """

    positioner: str
    """ Positioner name. """

    updateFreq: int
    """ Update frequency, in milliseconds. """

    frameCropx: int
    """ Starting X position of camera frame crop. """

    frameCropy: int
    """ Starting Y position of camera frame crop. """

    frameCropw: int
    """ Width of camera frame crop. """

    frameCroph: int
    """ Height of camera frame crop. """


    piKp: float
    """ Default kp value of feedback loop. """

    piKi: float
    """ Default ki value of feedback loop. """


@dataclass(frozen=False)
class AutofocusInfo:
    camera: str
    """ Detector name. """

    positioner: str
    """ Positioner name. """

    updateFreq: int
    """ Update frequency, in milliseconds. """

    frameCropx: int
    """ Starting X position of frame crop. """

    frameCropy: int
    """ Starting Y position of frame crop. """

    frameCropw: int
    """ Width of frame crop. """

    frameCroph: int
    """ Height of frame crop. """


@dataclass(frozen=False)
class ScanInfo:
    scanWidgetType: str
    """ Type of scan widget to generate: PointScan/MoNaLISA/Base/etc."""

    scanDesigner: str
    """ Name of the scan designer class to use. """

    scanDesignerParams: Dict[str, Any]
    """ Params to be read by the scan designer. """

    TTLCycleDesigner: str
    """ Name of the TTL cycle designer class to use. """

    TTLCycleDesignerParams: Dict[str, Any]
    """ Params to be read by the TTL cycle designer. """

    sampleRate: int
    """ Scan sample rate. """

    lineClockLine: Optional[Union[str, int]]
    """ Line for line clock output. ``null`` if not wanted or NI-DAQ is not used.
    If integer, it will be translated to "Dev1/port0/line{lineClockLine}".
    """

    frameClockLine: Optional[Union[str, int]]
    """ Line for frame clock output. ``null`` if not wanted or NI-DAQ is not used.
    If integer, it will be translated to "Dev1/port0/line{frameClockLine}".
    """

@dataclass(frozen=False)
class EtSTEDInfo:
    detectorFast: str
    """ Name of the STED detector to use. """

    detectorSlow: str
    """ Name of the widefield detector to use. """

    laserFast: str
    """ Name of the widefield laser to use. """


@dataclass(frozen=False)
class MicroscopeStandInfo:
    managerName: str
    """ Name of the manager to use. """

    rs232device: str
    """ Name of the rs232 device to use. """


@dataclass(frozen=False)
class NidaqInfo:
    timerCounterChannel: Optional[Union[str, int]] = None
    """ Output for Counter for timing purposes. If an integer is specified, it
    will be translated to "Dev1/ctr{timerCounterChannel}". """

    startTrigger: bool = False
    """ Boolean for start triggering for sync. """

    def getTimerCounterChannel(self):
        """ :meta private: """
        if isinstance(self.timerCounterChannel, int):
            return f'Dev1/ctr{self.timerCounterChannel}'  # for backwards compatibility
        else:
            return self.timerCounterChannel

@dataclass(frozen=False)
class PulseStreamerInfo:
    ipAddress: Optional[str] = None
    """ IP address of Pulse Streamer hardware. """

@dataclass(frozen=False)
class PyroServerInfo:
    name: Optional[str] = 'ImSwitchServer'
    host: Optional[
        str] = '0.0.0.0'  # - listen to all addresses on v6 # '0.0.0.0'- listen to all IP addresses # 127.0.0.1 - only locally
    port: Optional[int] = 54333
    active: Optional[bool] = False


@dataclass_json(undefined=Undefined.INCLUDE)
@dataclass
class SetupInfo:
    # default_factory seems to be required for the field to show up in autodocs for deriving classes
    detectors: Dict[str, DetectorInfo] = field(default_factory=dict)
    """ Detectors in this setup. This is a map from unique detector names to
    DetectorInfo objects. """

    lasers: Dict[str, LaserInfo] = field(default_factory=dict)
    """ Lasers in this setup. This is a map from unique laser names to
    LaserInfo objects. """

    LEDs: Dict[str, LEDInfo] = field(default_factory=dict)
    """ LEDs in this setup. This is a map from unique laser names to
    LEDInfo objects. """

    LEDMatrixs: Dict[str, LEDMatrixInfo] = field(default_factory=dict)
    """ LEDMatrixs in this setup. This is a map from unique LEDMatrix names to
    LEDMatrixInfo objects. """

    positioners: Dict[str, PositionerInfo] = field(default_factory=dict)
    """ Positioners in this setup. This is a map from unique positioner names
    to DetectorInfo objects. """

    rs232devices: Dict[str, RS232Info] = field(default_factory=dict)
    """ RS232 connections in this setup. This is a map from unique RS232
    connection names to RS232Info objects. Some detector/laser/positioner
    managers will require a corresponding RS232 connection to be referenced in
    their properties.
    """

    slm: Optional[SLMInfo] = field(default_factory=lambda: None)
    """ SLM settings. Required to be defined to use SLM functionality. """

    sim: Optional[SIMInfo] = field(default_factory=lambda: None)
    """ SIM settings. Required to be defined to use SIM functionality. """

    dpc: Optional[DPCInfo] = field(default_factory=lambda: None)
    """ DPC settings. Required to be defined to use DPC functionality. """

    objective: Optional[ObjectiveInfo] = field(default_factory=lambda: None)
    """ Objective settings. Required to be defined to use Objective functionality. """

    mct: Optional[MCTInfo] = field(default_factory=lambda: None)
    """ MCT settings. Required to be defined to use MCT functionality. """

    nidaq: NidaqInfo = field(default_factory=NidaqInfo)
    """ NI-DAQ settings. """

    roiscan: Optional[ROIScanInfo] = field(default_factory=lambda: None)
    """ ROIScan settings. Required to be defined to use ROIScan functionality. """

    lightsheet: Optional[LightsheetInfo] = field(default_factory=lambda: None)
    """ MCT settings. Required to be defined to use Lightsheet functionality. """

    webrtc: Optional[WebRTCInfo] = field(default_factory=lambda: None)
    """ WebRTC settings. Required to be defined to use WebRTC functionality. """

    hypha: Optional[HyphaInfo] = field(default_factory=lambda: None)
    """ Hypha settings. Required to be defined to use Hypha functionality. """

    mockxx: Optional[MockXXInfo] = field(default_factory=lambda: None)
    """ MockXX settings. Required to be defined to use MockXX functionality."""

    jetsonnano: Optional[JetsonNanoInfo] = field(default_factory=lambda: None)
    """ Jetson Nano settings for jetson nano. Required to be defined to use jetson nano functionality. """

    Stresstest: Optional[StresstestInfo] = field(default_factory=lambda: None)
    """ Stresstest settings. Required to be defined to use Stresstest functionality. """
    
    HistoScan: Optional[HistoScanInfo] = field(default_factory=lambda: None)
    """ HistoScan settings. Required to be defined to use HistoScan functionality. """

    Workflow: Optional[WorkflowInfo] = field(default_factory=lambda: None)
    """ Workflow settings. Required to be defined to use Workflow functionality. """

    FlowStop:  Optional[FlowStopInfo] = field(default_factory=lambda: None)
    """ FlowStop settings. Required to be defined to use FlowStop functionality. """

    Lepmon: Optional[LepmonInfo] = field(default_factory=lambda: None)
    """ Lepmon settings. Required to be defined to use Lepmon functionality. """

    Flatfield: Optional[FlatfieldInfo] = field(default_factory=lambda: None)
    """ Flatfield settings. Required to be defined to use Flatfield functionality. """

    PixelCalibration: Optional[PixelCalibrationInfo] = field(default_factory=lambda: None)
    """ PixelCalibration settings. Required to be defined to use PixelCalibration functionality. """

    experiment: Optional[ExperimentInfo] = field(default_factory=lambda: None)
    """ Experiment settings including OMERO configuration. Required to be defined for experiment functionality. """

    uc2Config: Optional[UC2ConfigInfo] = field(default_factory=lambda: None)
    """ UC2Config settings. Required to be defined to use UC2Config functionality. """

    ism: Optional[ISMInfo] = field(default_factory=lambda: None)
    """ ISM settings. Required to be defined to use ISM functionality. """

    focusLock: Optional[FocusLockInfo] = field(default_factory=lambda: None)
    """ Focus lock settings. Required to be defined to use focus lock
    functionality. """

    arkitekt: Optional[ArkitektInfo] = field(default_factory=lambda: None)
    """ Arkitekt integration settings. Required to be defined to use Arkitekt
    functionality. """

    fovLock: Optional[FOVLockInfo] = field(default_factory=lambda: None)
    """ Focus lock settings. Required to be defined to use fov lock
    functionality. """

    autofocus: Optional[AutofocusInfo] = field(default_factory=lambda: None)
    """ Autofocus settings. Required to be defined to use autofocus
    functionality. """

    scan: Optional[ScanInfo] = field(default_factory=lambda: None)
    """ Scan settings. Required to be defined to use scan functionality. """

    etSTED: Optional[EtSTEDInfo] = field(default_factory=lambda: None)
    """ EtSTED settings. Required to be defined to use etSTED functionality. """

    rotators: Optional[Dict[str, DeviceInfo]] = field(default_factory=lambda: None)
    """ Standa motorized rotator mounts settings. Required to be defined to use rotator functionality. """

    microscopeStand: Optional[MicroscopeStandInfo] = field(default_factory=lambda: None)
    """ Microscope stand settings. Required to be defined to use MotCorr widget. """

    nidaq: NidaqInfo = field(default_factory=NidaqInfo)
    """ NI-DAQ settings. """

    pulseStreamer: PulseStreamerInfo = field(default_factory=PulseStreamerInfo)
    """ Pulse Streamer settings. """

    pyroServerInfo: PyroServerInfo = field(default_factory=PyroServerInfo)


    _catchAll: CatchAll = None

    def add_attribute(self, attr_name, attr_value):
        # load all implugin-related setup infos and add them to the class
        # try to get it from the plugins
        # If there is a imswitch_sim_info, we want to add this as self.imswitch_sim_info to the
        # SetupInfo Class

        import pkg_resources
        for entry_point in pkg_resources.iter_entry_points('imswitch.implugins'):
            if entry_point.name == attr_name+"_info":
                ManagerClass = entry_point.load()
                ManagerDataClass = make_dataclass(entry_point.name.split("_info")[0], [(entry_point.name, ManagerClass)])
                setattr(self, entry_point.name.split("_info")[0], field(default_factory=ManagerDataClass))

    def getDevice(self, deviceName):
        """ Returns the DeviceInfo for a specific device.

        :meta private:
        """
        return self.getAllDevices()[deviceName]

    def getTTLDevices(self):
        """ Returns DeviceInfo from all devices that have a digitalLine.

        :meta private:
        """
        devices = {}
        i = 0
        for deviceInfos in self.lasers, self.detectors:
            deviceInfosCopy = deviceInfos.copy()
            for item in list(deviceInfosCopy):
                if deviceInfosCopy[item].getDigitalLine() is None:
                    del deviceInfosCopy[item]
            devices.update(deviceInfosCopy)
            i += 1

        return devices

    def getDetectors(self):
        """ :meta private: """
        devices = {}
        for deviceInfos in self.detectors:
            devices.update(deviceInfos)

        return devices

    def getAllDevices(self):
        """ :meta private: """
        devices = {}
        for deviceInfos in self.lasers, self.detectors, self.positioners:
            devices.update(deviceInfos)

        return devices

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
