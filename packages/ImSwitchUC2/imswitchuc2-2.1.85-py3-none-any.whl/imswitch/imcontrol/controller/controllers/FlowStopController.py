import numpy as np
import datetime
import tifffile as tif
import os
import platform
import subprocess
import cv2
from threading import Thread, Event
try:
    import NanoImagingPack as nip
    isNIP = True
except:
    isNIP = False
import time
from imswitch.imcommon.model import dirtools, APIExport
from imswitch.imcommon.framework import Signal, Worker, Mutex, Timer
from imswitch.imcontrol.view import guitools
from imswitch.imcommon.model import initLogger
from ..basecontrollers import LiveUpdatedController
from imswitch import IS_HEADLESS
from imswitch.imcontrol.model import SaveMode, SaveFormat

class FlowStopController(LiveUpdatedController):
    """ Linked to FlowStopWidget."""

    sigImageReceived = Signal()
    sigImagesTaken = Signal(int)
    sigIsRunning = Signal(bool)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._logger = initLogger(self, tryInheritParent=False)

        # load from config file in User/Documents/ImSwitchConfig
        self.wasRunning = self._master.FlowStopManager.defaultConfig["wasRunning"]
        self.defaultFlowRate = self._master.FlowStopManager.defaultConfig["flowRate"]
        self.defaultNumberOfFrames = self._master.FlowStopManager.defaultConfig["numberOfFrames"]
        self.defaultExperimentName = self._master.FlowStopManager.defaultConfig["experimentName"]
        self.defaultFrameRate = self._master.FlowStopManager.defaultConfig["frameRate"]
        self.defaultSavePath = self._master.FlowStopManager.defaultConfig["savePath"]
        self.defaultFileFormat = self._master.FlowStopManager.defaultConfig["fileFormat"]
        self.defaultIsRecordVideo = self._master.FlowStopManager.defaultConfig["isRecordVideo"]
        self.pumpAxis = self._master.FlowStopManager.defaultConfig["axisFlow"]
        self.focusAxis = self._master.FlowStopManager.defaultConfig["axisFocus"]
        self.defaultDelayTimeAfterRestart = self._master.FlowStopManager.defaultConfig["delayTimeAfterRestart"]
        self.mExperimentParameters = self._master.FlowStopManager.defaultConfig
        self.tSettle = 0.05
        self.imagesTaken = 0
        # select detectors
        allDetectorNames = self._master.detectorsManager.getAllDeviceNames()
        self.detectorFlowCam = self._master.detectorsManager[allDetectorNames[0]]

        self.is_measure = False

        # select light source and activate
        allIlluNames = self._master.lasersManager.getAllDeviceNames()
        self.ledSource = self._master.lasersManager[allIlluNames[0]]
        #self.ledSource.setValue(1023)
        self.ledSource.setEnabled(1)
        # connect camera and stage
        self.positionerName = self._master.positionersManager.getAllDeviceNames()[0]
        self.positioner = self._master.positionersManager[self.positionerName]

        # start live and adjust camera settings to auto exposure
        self.changeAutoExposureTime('auto')

        # Connect FlowStopWidget signals
        if not IS_HEADLESS:
            # Connect CommunicationChannel signals
            #self._commChannel.sigUpdateImage.connect(self.update)
            self._widget.sigSnapClicked.connect(self.snapImageFlowCam)
            self._widget.sigSliderFocusValueChanged.connect(self.changeFocus)
            self._widget.sigSliderPumpSpeedValueChanged.connect(self.changePumpSpeed)
            self._widget.sigExposureTimeChanged.connect(self.changeExposureTime)
            self._widget.sigGainChanged.connect(self.changeGain)
            self._widget.sigPumpDirectionToggled.connect(self.changePumpDirection)

            # Connect buttons
            self._widget.buttonStart.clicked.connect(self.startFlowStopExperimentByButton)
            self._widget.buttonStop.clicked.connect(self.stopFlowStopExperimentByButton)
            self._widget.pumpMovePosButton.clicked.connect(self.movePumpPos)
            self._widget.pumpMoveNegButton.clicked.connect(self.movePumpNeg)

        # start thread if it was funning
        if self.wasRunning:
            timeStamp = datetime.datetime.now().strftime("%Y_%m_%d-%H-%M-%S")
            experimentName = self.defaultExperimentName
            experimentDescription = ""
            uniqueId = np.random.randint(0, 2**16)
            numImages = self.defaultNumberOfFrames
            volumePerImage = self.defaultFlowRate
            timeToStabilize = self.tSettle
            delayToStart = self.defaultDelayTimeAfterRestart
            frameRate = self.defaultFrameRate
            filePath = self.defaultSavePath
            fileFormat = self.defaultFileFormat
            isRecordVideo = self.defaultIsRecordVideo
            self.startFlowStopExperiment(timeStamp, experimentName, experimentDescription,
                                         uniqueId, numImages, volumePerImage, timeToStabilize, delayToStart,
                                         frameRate, filePath, fileFormat, isRecordVideo)

    def startFlowStopExperimentByButton(self):
        """ Start FlowStop experiment. """
        self.is_measure=True
        self.mExperimentParameters = self._widget.getAutomaticImagingParameters()

        # parse the parameters from dict to single variables
        '''
        'timeStamp': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'experimentName': self.textEditExperimentName.text(),
        'experimentDescription': self.textEditExperimentDescription.text(),
        'uniqueId': self.textEditUniqueId.text(),
        'numImages': self.textEditNumImages.text(),
        'volumePerImage': self.textEditVolumePerImage.text(),
        'timeToStabilize': self.textEditTimeToStabilize.text(),
        '''
        timeStamp = datetime.datetime.now().strftime("%Y_%m_%d-%H-%M-%S") # overriding this: self.mExperimentParameters['timeStamp']
        experimentName = self.mExperimentParameters['experimentName']
        experimentDescription = self.mExperimentParameters['experimentDescription']
        uniqueId = self.mExperimentParameters['uniqueId']
        numImages = int(self.mExperimentParameters['numImages'])
        volumePerImage = float(self.mExperimentParameters['volumePerImage'])
        timeToStabilize = float(self.mExperimentParameters['timeToStabilize'])
        fileFormat = self.defaultFileFormat
        isRecordVideo = self.defaultIsRecordVideo
        pumpSpeed = float(self.mExperimentParameters['pumpSpeed'])
        self._widget.buttonStart.setEnabled(False)
        self._widget.buttonStop.setEnabled(True)
        self._widget.buttonStop.setStyleSheet("background-color: red")
        self._widget.buttonStart.setStyleSheet("background-color: grey")
        self.startFlowStopExperiment(timeStamp = timeStamp, experimentName = experimentName,
                                     experimentDescription = experimentDescription, uniqueId = uniqueId,
                                     numImages = numImages, volumePerImage = volumePerImage,
                                     timeToStabilize = timeToStabilize, delayToStart = 0, frameRate = 1,
                                     filePath = self.defaultSavePath, fileFormat = fileFormat,
                                     isRecordVideo = isRecordVideo,
                                     pumpSpeed = pumpSpeed)


    @APIExport()
    def getStatus(self) -> list:
        return [self.is_measure, self.imagesTaken]

    @APIExport()
    def getExperimentParameters(self) -> dict:
        if not IS_HEADLESS:
            self.mExperimentParameters = self._widget.getAutomaticImagingParameters()
        else:
            self.mExperimentParameters["timeStamp"] = datetime.datetime.now().strftime("%Y_%m_%d-%H-%M-%S")
        return self.mExperimentParameters

    @APIExport()
    def isRunning(self) -> bool:
        return self.is_measure

    @APIExport(runOnUIThread=True)
    def startFlowStopExperimentFastAPI(self, timeStamp: str, experimentName: str, experimentDescription: str,
                                        uniqueId: str, numImages: int, volumePerImage: float, timeToStabilize: float,
                                        delayToStart: float=1, frameRate: float=1, filePath: str="./",
                                        fileFormat: str= "JPG", isRecordVideo: bool = True,
                                        pumpSpeed: float = 10000):
        try:uniqueId = int(uniqueId)
        except:uniqueId = np.random.randint(0, 2**16)

        # Store the parameters
        self.mExperimentParameters = {
            'timeStamp': timeStamp,
            'experimentName': experimentName,
            'experimentDescription': experimentDescription,
            'uniqueId': uniqueId,
            'numImages': numImages,
            'volumePerImage': volumePerImage,
            'timeToStabilize': timeToStabilize,
            'delayToStart': delayToStart,
            'frameRate': frameRate,
            'filePath': filePath,
            'fileFormat': fileFormat,
            'isRecordVideo': isRecordVideo,
            'pumpSpeed': pumpSpeed
        }
        """ Start FlowStop experiment. """
        self.startFlowStopExperiment(timeStamp, experimentName, experimentDescription,
                                        uniqueId, numImages, volumePerImage, timeToStabilize,
                                        delayToStart, frameRate, filePath, fileFormat, isRecordVideo,
                                        pumpSpeed)
        return self.mExperimentParameters

    def startFlowStopExperiment(self, timeStamp: str, experimentName: str, experimentDescription: str,
                                uniqueId: str, numImages: int, volumePerImage: float, timeToStabilize: float,
                                delayToStart: float=1, frameRate: float=1, filePath: str="./",
                                fileFormat: str= "JPG", isRecordVideo: bool = True,
                                pumpSpeed: float = 10000):
        try:uniqueId = int(uniqueId)
        except:uniqueId = np.random.randint(0, 2**16)
        """ Start FlowStop experiment. """
        self.thread = Thread(target=self.flowExperimentThread,
                             name="FlowStopExperiment",
                             args=(timeStamp, experimentName, experimentDescription,
                                   uniqueId, numImages, volumePerImage, timeToStabilize,
                                   delayToStart, frameRate, filePath, fileFormat, isRecordVideo,
                                   pumpSpeed))

        self.thread.start()

    def stopFlowStopExperimentByButton(self):
        """ Stop FlowStop experiment. """
        self._widget.buttonStart.setEnabled(True)
        self._widget.buttonStop.setEnabled(False)
        self._widget.buttonStop.setStyleSheet("background-color: grey")
        self._widget.buttonStart.setStyleSheet("background-color: green")
        self.stopFlowStopExperiment()

    @APIExport(runOnUIThread=True)
    def stopPump(self):
        self.positioner.stopAll()

    @APIExport(runOnUIThread=True)
    def movePump(self, value: float = 0.0, speed: float = 10000.0):
        self.positioner.move(value=value, speed=speed, axis=self.pumpAxis, is_absolute=False, is_blocking=False)

    @APIExport(runOnUIThread=True)
    def moveFocus(self, value: float = 0.0, speed: float = 10000.0):
        self.positioner.move(value=value, speed=speed, axis=self.focusAxis, is_absolute=False, is_blocking=False)

    @APIExport(runOnUIThread=True)
    def stopFocus(self):
        self.positioner.stopAll()

    @APIExport(runOnUIThread=True)
    def getCurrentFrameNumber(self):
        return self.imagesTaken

    @APIExport(runOnUIThread=True)
    def setIlluIntensity(self, value: float = 0.0):
        self.ledSource.setValue(value)

    @APIExport(runOnUIThread=True)
    def stopFlowStopExperiment(self):
        self.sigIsRunning.emit(False)
        self.is_measure=False
        if not IS_HEADLESS:
            self._widget.buttonStart.setEnabled(True)
            self._widget.buttonStop.setEnabled(False)
            self._widget.buttonStop.setStyleSheet("background-color: grey")
            self._widget.buttonStart.setStyleSheet("background-color: green")

    def flowExperimentThread(self, timeStamp: str, experimentName: str,
                             experimentDescription: str, uniqueId: str,
                             numImages: int, volumePerImage: float,
                             timeToStabilize: float, delayToStart: float=0,
                             frameRate: float=1, filePath:str="./",
                             fileFormat="TIF", isRecordVideo: bool = True,
                             pumpSpeed: float = 10000):
        ''' FlowStop experiment thread.
        The device captures images periodically by moving the pump at n-steps / ml, waits for a certain time
        and then moves on to the next step. The experiment is stopped when the user presses the stop button or
        it acquried N-images.

        User supplied parameters:

        '''
        self.isRecordVideo = isRecordVideo
        self._logger.debug("Starting the FlowStop experiment thread in {delayToStart} seconds.")
        time.sleep(abs(delayToStart))
        self._commChannel.sigStartLiveAcquistion.emit(True)
        self.is_measure = True
        if numImages < 0: numImages = np.inf
        self.imagesTaken = 0
        drivePath = dirtools.UserFileDirs.Data
        dirPath = os.path.join(drivePath, 'recordings', timeStamp)
        self._logger.debug(dirPath)
        if not os.path.exists(dirPath):
            os.makedirs(dirPath)

        # create the video writer object
        videoFrameRate = 5
        videoBitrate = 4000000
        if self.isRecordVideo:
            self.video_safe = VideoSafe(self.detectorFlowCam.getLatestFrame, output_folder=dirPath, frame_rate=videoFrameRate, bitrate=videoBitrate)
            self.video_safe.start()
        self.sigIsRunning.emit(True)
        while True:
            if dirtools.getDiskusage()>.95:
                self.is_measure = False
                self._logger.error("DISK IS FULL. PLEASE DELETE FILES!!!")
            currentTime = time.time()
            self.imagesTaken += 1
            self.sigImagesTaken.emit(self.imagesTaken)
            if self.imagesTaken > numImages: break
            if self.is_measure:
                stepsToMove = volumePerImage
                self.positioner.move(value=stepsToMove, speed=pumpSpeed, axis=self.pumpAxis, is_absolute=False, is_blocking=True, timeout=1)
                time.sleep(timeToStabilize)
                metaData = {
                    'timeStamp': timeStamp,
                    'experimentName': experimentName,
                    'experimentDescription': experimentDescription,
                    'uniqueId': uniqueId,
                    'numImages': numImages,
                    'volumePerImage': volumePerImage,
                    'timeToStabilize': timeToStabilize,
                }
                self.setSharedAttr('FlowStop', _metaDataAttr, metaData)


                # save image
                mFileName = f'{timeStamp}_{experimentName}_{uniqueId}_{self.imagesTaken}'
                mFilePath = os.path.join(dirPath, mFileName)
                self.snapImageFlowCam(mFilePath, metaData, fileFormat=fileFormat)
                self.sigImagesTaken.emit(self.imagesTaken)
                self._logger.debug(f"Image {self.imagesTaken} saved to {mFilePath}.{fileFormat}")

                # maintain framerate
                while (time.time()-currentTime)<(1/frameRate):
                    time.sleep(0.05)
                if not IS_HEADLESS:
                    self._widget.labelStatusValue.setText(f'Running: {self.imagesTaken+1}/{numImages}')
            else:
                break

        # stop the video writer
        if self.isRecordVideo:
            self.video_safe.stop()

        # restet the GUI
        self.stopFlowStopExperiment()

    def setSharedAttr(self, laserName, attr, value):
        self.settingAttr = True
        try:
            self._commChannel.sharedAttrs[(_attrCategory, laserName, attr)] = value
        finally:
            self.settingAttr = False

    @APIExport(runOnUIThread=True)
    def snapImageFlowCam(self, fileName=None, metaData={}, fileFormat="JPG"):
        """ Snap image. """
        if fileName is None or not fileName:
            fileName  = datetime.datetime.now().strftime("%Y_%m_%d-%H-%M-%S")

        if fileFormat == "TIF":
            # save as tif
            mFrame = self.detectorFlowCam.getLatestFrame()
            if mFrame is None:
                self._logger.warning("No frame received from the camera.")
                return
            tif.imwrite(fileName, mFrame, append=False)
        elif fileFormat == "JPG":
            # save as JPEG
            mFrame = self.detectorFlowCam.getLatestFrame()
            if mFrame is None:
                self._logger.warning("No frame received from the camera.")
                return
            if not cv2.imwrite(fileName+".jpg", mFrame):
                self._logger.warning("Frame could not be saved using cv2 jpeg")
                self._logger.warning("mFrame is None: "+str(mFrame is None))
                try:self._logger.warning("mFrame shape: "+str(mFrame.shape))
                except: pass
                return
        elif fileFormat == "PNG":
            pngFormat = SaveFormat.PNG
            saveMode = SaveMode.Disk
            self._master.recordingManager.snap([self.detectorFlowCam], saveMode=saveMode, saveFormat=pngFormat, savename=fileName, attrs=metaData)
        else:
            self._logger.warning("Nothing saved, no fileformat selected")

    def movePumpPos(self):
        self.positioner.moveRelative((0,0,1*self.directionPump))

    def movePumpNeg(self):
        self.positioner.moveRelative((0,0,-1*self.directionPump))

    def changeFocus(self, value):
        """ Change focus. """
        self.positioner.move

    def changePumpSpeed(self, value):
        """ Change pump speed. """
        self.speedPump = value
        self.positioner.moveForever(speed=(self.speedPump,self.speedRotation,0),is_stop=False)

    @APIExport(runOnUIThread=True)
    def changeExposureTime(self, value):
        """ Change exposure time. """
        self.detector.setParameter(name="exposure", value=value)

    @APIExport(runOnUIThread=True)
    def changeAutoExposureTime(self, value):
        """ Change auto exposure time. """
        try:
            self.detectorFlowCam.setParameter(name="exposure_mode", value=value)
        except Exception as e:
            self._logger.error(f"Could not set auto exposure mode: {e}")

    def changeGain(self, value):
        """ Change gain. """
        self.detectorFlowCam.setGain(value)

    def changePumpDirection(self, value):
        """ Change pump direction. """
        self.directionPump = value
        self.positioner.moveForever(speed=(self.speedPump,self.speedRotation,0),is_stop=False)

    def __del__(self):
        self.is_measure=False
        if hasattr(super(), '__del__'):
            super().__del__()

    def displayImage(self, im):
        """ Displays the image in the view. """
        self._widget.setImage(im)




class VideoSafe:
    def __init__(self, frame_provider, output_folder, frame_rate=5, bitrate=4000000):
        """
        Initializes the VideoSafe class.

        Parameters:
        frame_provider (function): Function that returns a numpy array frame when called.
        output_folder (str): Directory to save the video files.
        frame_rate (int): Frames per second.
        bitrate (int): Video bitrate.
        """
        self.frame_provider = frame_provider
        self.output_folder = output_folder
        self.frame_rate = frame_rate
        self.bitrate = bitrate
        self.max_frames = 1000
        self.stop_event = Event()
        self.thread = None
        self.video_writer = None
        self.frame_count = 0

        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

    def _get_video_writer(self):
        """
        Initializes a new video writer object.

        Returns:
        cv2.VideoWriter: The video writer object.
        """
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        video_filename = os.path.join(self.output_folder, f"{timestamp}.mp4")
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        frame = self.frame_provider()
        height, width = frame.shape[:2]
        video_writer = cv2.VideoWriter(video_filename, fourcc, self.frame_rate, (width, height))

        # Set the bitrate if possible (note: OpenCV might not support setting bitrate directly)
        #if hasattr(cv2, 'CAP_PROP_BITRATE'):
        #    video_writer.set(cv2.CAP_PROP_BITRATE, self.bitrate)

        return video_writer

    def _write_video(self):
        """
        Continuously writes frames to the video file until stopped.
        """
        self.video_writer = self._get_video_writer()
        while not self.stop_event.is_set():
            frame = self.frame_provider()
            #https://stackoverflow.com/questions/30509573/writing-an-mp4-video-using-python-opencv
            frame = cv2.cvtColor(cv2.convertScaleAbs(frame), cv2.COLOR_GRAY2BGR)
            self.video_writer.write(frame)
            self.frame_count += 1
            if self.frame_count >= self.max_frames:
                self.video_writer.release()
                self.video_writer = self._get_video_writer()
                self.frame_count = 0
            time.sleep(1 / self.frame_rate)

    def start(self):
        """
        Starts the video acquisition in a separate thread.
        """
        if self.thread is None:
            self.stop_event.clear()
            self.thread = Thread(target=self._write_video)
            self.thread.start()

    def stop(self):
        """
        Stops the video acquisition.
        """
        if self.thread is not None:
            self.stop_event.set()
            self.thread.join()
            self.thread = None
            if self.video_writer is not None:
                self.video_writer.release()

_attrCategory = 'Laser'
_metaDataAttr = 'metaData'
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
