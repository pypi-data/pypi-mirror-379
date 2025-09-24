import os
import threading
from datetime import datetime
import time
import cv2
import matplotlib.pyplot as plt
import numpy as np
import scipy
import scipy.ndimage as ndi
import scipy.signal as signal
import skimage.transform as transform
import tifffile as tif
from imswitch import IS_HEADLESS
from imswitch.imcommon.framework import Signal, Thread, Worker, Mutex, Timer
from imswitch.imcommon.model import dirtools, initLogger, APIExport
from skimage.registration import phase_cross_correlation
from ..basecontrollers import ImConWidgetController
from fastapi.responses import FileResponse


class LightsheetController(ImConWidgetController):
    """Linked to LightsheetWidget."""
    sigImageReceived = Signal(np.ndarray)
    sigSliderIlluValueChanged = Signal(float)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._logger = initLogger(self)

        self.lightsheetTask = None
        self.lightsheetStack = np.ones((1,1,1))
        self.mFilePath = None
        # select detectors
        allDetectorNames = self._master.detectorsManager.getAllDeviceNames()
        self.detector = self._master.detectorsManager[allDetectorNames[0]]

        # select lasers and add to gui
        self.lasers = self._master.lasersManager.getAllDeviceNames()
        self.laser = self.lasers[0]
        self.stageName = self._master.positionersManager.getAllDeviceNames()[0]
        self.stages = self._master.positionersManager[self.stageName]
        self.isLightsheetRunning = False
        
         

        # connect signals
        self.sigImageReceived.connect(self.displayImage)
        self._commChannel.sigStartLightSheet.connect(self.performScanningRecording)
        self._commChannel.sigStopLightSheet.connect(self.stopLightsheet)
        self._commChannel.sigUpdateMotorPosition.connect(self.updateAllPositionGUI)

        if IS_HEADLESS:
            return
        self._widget.startButton.clicked.connect(self.startLightsheet)
        self._widget.stopButton.clicked.connect(self.stopLightsheet)
        self._widget.setAvailableIlluSources(self.lasers)
        self._widget.setAvailableStageAxes(self.stages.axes)
        self._widget.sigSliderIlluValueChanged.connect(self.valueIlluChanged)

        # Connect all GUI elements from the SCAN tab
        self._widget.button_scan_xyz_start.clicked.connect(self.onButtonScanStart)
        self._widget.button_scan_xyz_stop.clicked.connect(self.onButtonScanStop)
        self._widget.buttonXY_up.clicked.connect(self.onButtonXYUp)
        self._widget.buttonXY_down.clicked.connect(self.onButtonXYDown)
        self._widget.buttonXY_left.clicked.connect(self.onButtonXYLeft)
        self._widget.buttonXY_right.clicked.connect(self.onButtonXYRight)
        self._widget.buttonXY_zero.clicked.connect(self.onButtonXYZero)
        self._widget.buttonFocus_up.clicked.connect(self.onButtonFocusUp)
        self._widget.buttonFocus_down.clicked.connect(self.onButtonFocusDown)
        self._widget.buttonSample_fwd.clicked.connect(self.onButtonSampleForward)
        self._widget.buttonSample_bwd.clicked.connect(self.onButtonSampleBackward)
        self._widget.buttonFocus_zero.clicked.connect(self.onButtonFocusZero)
        self._widget.button_scan_x_min_snap.clicked.connect(self.onButtonScanXMin)
        self._widget.button_scan_x_max_snap.clicked.connect(self.onButtonScanXMax)
        self._widget.button_scan_y_min_snap.clicked.connect(self.onButtonScanYMin)
        self._widget.button_scan_y_max_snap.clicked.connect(self.onButtonScanYMax)
        self._widget.button_scan_z_min_snap.clicked.connect(self.onButtonScanZMin)
        self._widget.button_scan_z_max_snap.clicked.connect(self.onButtonScanZMax)

        #self._widget.buttonRotation_minus.clicked.connect(self.onButtonRotationMinus)
        #self._widget.buttonRotation_plus.clicked.connect(self.onButtonRotationPlus)
        #self._widget.buttonRotation_zero.clicked.connect(self.onButtonRotationZero)

    # Event handler methods
    def onButtonScanStart(self):
        if IS_HEADLESS: # TODO: implement headless parameters
            return
        mScanParams = self._widget.get_scan_parameters()
        # returns => (self.scan_x_min[1].value(), self.scan_x_max[1].value(), self.scan_y_min[1].value(), self.scan_y_max[1].value(),
        # self.scan_z_min[1].value(), self.scan_z_max[1].value(), self.scan_overlap[1].value())

        # compute the spacing between xy tiles
        nPixels = self.detector.shape[0]
        pixelSize = self.detector.pixelSizeUm[-1]
        scanOverlap = mScanParams['overlap']*0.01

        # compute the number of pixels to move in x and y direction
        xrange = mScanParams['x_max']-mScanParams['x_min']
        yrange = mScanParams['y_max']-mScanParams['y_min']
        xSpacing = nPixels*pixelSize*(1-scanOverlap)
        ySpacing = nPixels*pixelSize*(1-scanOverlap)
        nTilesX = int(np.ceil(xrange/xSpacing))
        nTilesY = int(np.ceil(yrange/ySpacing))

        # compute x and y scan positions
        xyPositions = []
        for i in range(nTilesX):
            for j in range(nTilesY):
                xPosition = mScanParams['x_min']+i*xSpacing
                yPosition = mScanParams['y_min']+j*ySpacing
                xyPositions.append((int(xPosition), int(yPosition)))

        # perform the scanning in the background
        def performScanning(xyPositions, zMin, zMax, speed, axis, illuSource, illuValue):
            if not self.isLightsheetRunning:
                self.isLightsheetRunning = True
                for x, y in xyPositions:
                    self.lightsheetThread(zMin, zMax, x, y, speed, axis, illuSource, illuValue)
                self.isLightsheetRunning = False
        self._logger.info("Scan started")
        mThread = threading.Thread(target=performScanning, args=(xyPositions, mScanParams['z_min'], mScanParams['z_max'], mScanParams['speed'], mScanParams['stage_axis'], mScanParams['illu_source'], mScanParams['illu_value']))
        mThread.start()



    def onButtonScanStop(self):
        self._logger.debug("Scan stopped")
        self.isLightsheetRunning = False

    def onButtonXYUp(self):
        if IS_HEADLESS:  # TODO: implement headless parameters
            return
        mStepsizeXY,_ = self._widget.get_step_size_xy_zf()
        self._master.positionersManager.execOn(self.stageName, lambda c: c.move(axis="X", value=mStepsizeXY, is_absolute=False, is_blocking=False))

    def onButtonXYDown(self):
        mStepsizeXY,_ = self._widget.get_step_size_xy_zf()
        self.stages.move(value=-mStepsizeXY, axis="X", is_absolute=False, is_blocking=False)

    def onButtonXYLeft(self):
        mStepsizeXY,_ = self._widget.get_step_size_xy_zf()
        self.stages.move(value=mStepsizeXY, axis="Y", is_absolute=False, is_blocking=False)

    def onButtonXYRight(self):
        mStepsizeXY,_ = self._widget.get_step_size_xy_zf()
        self.stages.move(value=-mStepsizeXY, axis="Y", is_absolute=False, is_blocking=False)

    def onButtonXYZero(self):
        print("XY position reset")

    def onButtonFocusUp(self):
        _, mStepsizeXY = self._widget.get_step_size_xy_zf()
        self.stages.move(value=mStepsizeXY, axis="Z", is_absolute=False, is_blocking=False)

    def onButtonFocusDown(self):
        _, mStepsizeXY = self._widget.get_step_size_xy_zf()
        self.stages.move(value=-mStepsizeXY, axis="Z", is_absolute=False, is_blocking=False)

    def onButtonSampleForward(self):
        _, mStepsizeXY = self._widget.get_step_size_xy_zf()
        self.stages.move(value=mStepsizeXY, axis="A", is_absolute=False, is_blocking=False)

    def onButtonSampleBackward(self):
        _, mStepsizeXY = self._widget.get_step_size_xy_zf()
        self.stages.move(value=-mStepsizeXY, axis="A", is_absolute=False, is_blocking=False)

    def onButtonFocusZero(self):
        print("Focus position reset")

    def onButtonRotationMinus(self):
        print("Rotation decreased")

    def onButtonRotationPlus(self):
        print("Rotation increased")

    def onButtonRotationZero(self):
        print("Rotation reset")

    def getPositionByAxis(self, axis):
        allPositions = self.stages.getPosition()
        return allPositions[axis]

    def onButtonScanXMin(self):
        mPosition = self.getPositionByAxis("X")
        self._widget.set_scan_x_min(mPosition)

    def onButtonScanXMax(self):
        mPosition = self.getPositionByAxis("X")
        self._widget.set_scan_x_max(mPosition)

    def onButtonScanYMin(self):
        mPosition = self.getPositionByAxis("Y")
        self._widget.set_scan_y_min(mPosition)

    def onButtonScanYMax(self):
        mPosition = self.getPositionByAxis("Y")
        self._widget.set_scan_y_max(mPosition)

    def onButtonScanZMin(self):
        mPosition = self.getPositionByAxis("Z")
        self._widget.set_scan_z_min(mPosition)

    def onButtonScanZMax(self):
        mPosition = self.getPositionByAxis("Z")
        self._widget.set_scan_z_max(mPosition)

    def updateAllPositionGUI(self):
        #allPositions = self.stages.getPosition() # TODO: Necesllary?
        #mPositionsXYZ = (allPositions["X"], allPositions["Y"], allPositions["Z"])
        #self._widget.updatePosition(mPositionsXYZ)
        #self._commChannel.sigUpdateMotorPosition.emit()
        pass
        #TODO: This needs an update!

    def displayImage(self, lightsheetStack):
        # a bit weird, but we cannot update outside the main thread
        if IS_HEADLESS:
            return
        name = "Lightsheet Stack"
        # subsample stack
        # if the stack is too large, we have to subsample it
        if lightsheetStack.shape[0] > 200:
            subsample = 10
            lightsheetStack = lightsheetStack[::subsample,:,:]
        if not IS_HEADLESS:
            return self._widget.setImage(np.uint16(lightsheetStack ), colormap="gray", name=name, pixelsize=(20,1,1), translation=(0,0,0))

    def valueIlluChanged(self):
        if IS_HEADLESS:
            return
        illuSource = self._widget.getIlluminationSource()
        illuValue = self._widget.illuminationSlider.value()
        self._master.lasersManager
        if not self._master.lasersManager[illuSource].enabled:
            self._master.lasersManager[illuSource].setEnabled(1)

        illuValue = illuValue/100*self._master.lasersManager[illuSource].valueRangeMax
        self._master.lasersManager[illuSource].setValue(illuValue)

    def startLightsheet(self):
        if IS_HEADLESS:
            return
        minPos = self._widget.getMinPosition()
        maxPos = self._widget.getMaxPosition()
        speed = self._widget.getSpeed()
        illuSource = self._widget.getIlluminationSource()
        stageAxis = self._widget.getStageAxis()

        self._widget.startButton.setEnabled(False)
        self._widget.stopButton.setEnabled(True)
        self._widget.startButton.setText("Running")
        self._widget.stopButton.setText("Stop")
        self._widget.stopButton.setStyleSheet("background-color: red")
        self._widget.startButton.setStyleSheet("background-color: green")

        self.performScanningRecording(minPos, maxPos, speed, stageAxis, illuSource, 0)

    @APIExport()
    def setGalvo(self, channel:int=1, frequency:float=10, offset:float=0, amplitude:float=1, clk_div:int=0, phase:int=0, invert:int=1):
        '''Sets the galvo parameters for the lightsheet.'''
        if not self.isLightsheetRunning:
            try:
                self._master.lasersManager[self.laser].setGalvo(channel=channel, frequency=frequency, offset=offset, amplitude=amplitude, clk_div=clk_div, phase=phase, invert=invert)
                self._logger.info(f"Set galvo parameters: channel={channel}, frequency={frequency}, offset={offset}, amplitude={amplitude}, clk_div={clk_div}, phase={phase}, invert={invert}")
            except Exception as e:
                self._logger.error(f"Error setting galvo parameters: {e}")
        else:
            self._logger.warning("Cannot set galvo parameters while lightsheet is running.")
            
            
    @APIExport()
    def performScanningRecording(self, minPos:int=0, maxPos:int=1000, speed:int=1000, axis:str="A", illusource:int=-1, illuvalue:int=512):
        if not self.isLightsheetRunning:

            # check parameters
            if axis not in ("A", "X", "Y", "Z"):
                axis = "A"
            # use default illumination source if not selectd
            if illusource is None or illusource==-1 or illusource not in self._master.lasersManager.getAllDeviceNames():
                illusource = self._master.lasersManager.getAllDeviceNames()[0]

            #initialPosition = self.stages.getPosition()[axis]

            self.isLightsheetRunning = True
            if self.lightsheetTask is not None:
                self.lightsheetTask.join()
                del self.lightsheetTask
            self.lightsheetTask = threading.Thread(target=self.lightsheetThread, args=(minPos, maxPos, None, None, speed, axis, illusource, illuvalue))
            self.lightsheetTask.start()

    @APIExport()
    def returnLastLightsheetStackPath(self) -> str:
        '''Returns the path of the last saved lightsheet stack.'''
        if self.mFilePath is not None:
            return self.mFilePath
        else:
            return "No stack available yet"

    def lightsheetThread(self, minPosZ, maxPosZ, posX=None, posY=None, speed=10000, axis="A", illusource=None, illuvalue=None, isSave=True):
        '''Performs a lightsheet scan.'''
        self._logger.debug("Lightsheet thread started.")
        # TODO Have button for is save
        if posX is not None:
            self.stages.move(value=posX, axis="X", is_absolute=True, is_blocking=True)
        if posY is not None:
            self.stages.move(value=posY, axis="Y", is_absolute=True, is_blocking=True)
        self.detector.startAcquisition()
        # move to minPos
        self.stages.move(value=minPosZ, axis=axis, is_absolute=False, is_blocking=True)
        time.sleep(1)
        # now start acquiring images and move the stage in Background
        controller = MovementController(self.stages)
        controller.move_to_position(maxPosZ+np.abs(minPosZ), axis, speed, is_absolute=False)

        iFrame = 0
        allFrames = []
        while self.isLightsheetRunning:
            # Todo: Need to ensure thatwe have the right pattern displayed and the buffer is free - this heavily depends on the exposure time..
            mFrame = None
            lastFrameNumber = -1
            timeoutFrameRequest = .3 # seconds # TODO: Make dependent on exposure time
            cTime = time.time()
            frameSync = 2
            while(1):
                # get frame and frame number to get one that is newer than the one with illumination off eventually
                mFrame, currentFrameNumber = self.detector.getLatestFrame(returnFrameNumber=True)
                if lastFrameNumber==-1:
                    # first round
                    lastFrameNumber = currentFrameNumber
                if time.time()-cTime> timeoutFrameRequest:
                    # in case exposure time is too long we need break at one point
                    break
                if currentFrameNumber <= lastFrameNumber+frameSync:
                    time.sleep(0.01) # off-load CPU
                else:
                    break

            if mFrame is not None and mFrame.shape[0] != 0:
                allFrames.append(mFrame.copy())
            if controller.is_target_reached():
                break

            iFrame += 1
            # self._logger.debug(iFrame)


        # move back to initial position
        self.stages.move(value=-maxPosZ, axis=axis, is_absolute=False, is_blocking=True)

        # do something with the frames
        def displayAndSaveImageStack(isSave):
            # retreive positions and store the data if necessary
            pixelSizeZ = (maxPosZ-minPosZ)/len(allFrames)
            pixelSizeXY = self.detector.pixelSizeUm[-1]
            allPositions = self.stages.getPosition()
            posX = allPositions["X"]
            posY = allPositions["Y"]
            posZ = allPositions["Z"]
            if isSave:
                # save image stack with metadata
                mDate = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
                mExtension = "tif"
                mFileName = "lightsheet_stack_x_{posX}_y_{posY}_z_{posZ}_pz_{pixelSizeZ}_pxy_{pixelSizeXY}"
                self.mFilePath = self.getSaveFilePath(mDate, mFileName, mExtension)
                self._logger.info(f"Saving lightsheet stack to {self.mFilePath}")
                tif.imwrite(self.mFilePath, self.lightsheetStack)

        if len(allFrames) == 0:
            self._logger.error("No frames captured.")
            return
        self.lightsheetStack = np.array(allFrames).copy()
        saveImageThread = threading.Thread(target=displayAndSaveImageStack, args =(isSave,))
        saveImageThread.start()
        self.stopLightsheet()
        if not IS_HEADLESS: self.sigImageReceived.emit(self.lightsheetStack)

    def getSaveFilePath(self, date, filename, extension):
        mFilename =  f"{date}_{filename}.{extension}"
        dirPath  = os.path.join(dirtools.UserFileDirs.Data, 'recordings', date)
        newPath = os.path.join(dirPath,mFilename)

        if not os.path.exists(dirPath):
            os.makedirs(dirPath)

        return newPath

    @APIExport()
    def getLatestLightsheetStackAsTif(self):
        """
        If there is a lightsheet stack available, return it as a TIFF file for download.
        """
        if self.mFilePath is not None and os.path.exists(self.mFilePath):
            # Return the file as a response for download
            return FileResponse(
                path=self.mFilePath,
                media_type="application/octet-stream",
                filename=os.path.basename(self.mFilePath)
            )
        else:
            # Return an error message if the file is not available
            return {"error": "No lightsheet stack available"}

    @APIExport()
    def getIsLightsheetRunning(self):
        return self.isLightsheetRunning

    def stopLightsheet(self):
        self.isLightsheetRunning = False
        if IS_HEADLESS:
            return
        self._widget.startButton.setEnabled(True)
        self._widget.stopButton.setEnabled(False)
        self._widget.illuminationSlider.setValue(0)
        illuSource = self._widget.getIlluminationSource()
        if not self._master.lasersManager[illuSource].enabled:
            self._master.lasersManager[illuSource].setEnabled(0)
        self._widget.startButton.setText("Start")
        self._widget.stopButton.setText("Stopped")
        self._widget.stopButton.setStyleSheet("background-color: green")
        self._widget.startButton.setStyleSheet("background-color: red")
        self._logger.debug("Lightsheet scanning stopped.")



class MovementController:
    def __init__(self, stages):
        self.stages = stages
        self.target_reached = False
        self.target_position = None
        self.axis = None

    def move_to_position(self, minPos, axis, speed, is_absolute):
        self.target_position = minPos
        self.speed = speed
        self.is_absolute = is_absolute
        self.axis = axis
        thread = threading.Thread(target=self._move)
        thread.start()

    def _move(self):
        self.target_reached = False
        self.stages.move(value=self.target_position, axis=self.axis, speed=self.speed, is_absolute=self.is_absolute, is_blocking=True)
        self.target_reached = True

    def is_target_reached(self):
        return self.target_reached

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
