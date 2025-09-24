import numpy as np
try:
    import NanoImagingPack as nip
    isNIP = True
except:
    isNIP = False
import time
import threading
import collections

from imswitch.imcommon.framework import Signal, Thread, Worker, Mutex, Timer
from imswitch.imcontrol.view import guitools
from imswitch.imcommon.model import initLogger
from ..basecontrollers import LiveUpdatedController
from imswitch import IS_HEADLESS


class HoliSheetController(LiveUpdatedController):
    """ Linked to HoliSheetWidget."""

    sigImageReceived = Signal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._logger = initLogger(self, tryInheritParent=False)
        self.mWavelength = 488*1e-9
        self.NA=.3
        self.k0 = 2*np.pi/(self.mWavelength)
        self.pixelsize = 3.45*1e-6
        self.PSFpara = nip.PSF_PARAMS()
        self.PSFpara.wavelength = self.mWavelength
        self.PSFpara.NA=self.NA
        self.PSFpara.pixelsize = self.pixelsize

        self.dz = 40*1e-3

        # Parameters for monitoring the pressure
        self.tMeasure  = 0.2 # sampling rate of measure pressure
        self.is_measure = True
        self.pressureValue  = 0
        self.buffer = 100
        self.currPoint = 0
        self.setPointData = np.zeros((self.buffer,2))
        self.timeData = np.zeros(self.buffer)
        self.startTime = time.time()

        # settings for the controller
        self.controlTarget = 500
        # Hard-coded PID values..
        self.Kp = 5
        self.Ki = 0.1
        self.Kd = .5
        self.PIDenabled = False

        # Motor properties
        self.speedPump = .01 # steps/s
        self.speedRotation = .01 # steps/s
        self.stepsPerRotation = 200*32 # for microstepping
        self.tRoundtripRotation = self.stepsPerRotation/self.speedRotation

        # Prepare image computation worker
        self.imageComputationWorker = self.HoliSheetImageComputationWorker()
        self.imageComputationWorker.set_pixelsize(self.pixelsize)
        self.imageComputationWorker.set_dz(self.dz)
        self.imageComputationWorker.set_PSFpara(self.PSFpara)
        #self.imageComputationWorker.sigHoliSheetImageComputed.connect(self.displayImage) # TODO: Why not poassible to connect this signal?

        if IS_HEADLESS: return
        self.imageComputationThread = Thread()
        self.imageComputationWorker.moveToThread(self.imageComputationThread)
        self.sigImageReceived.connect(self.imageComputationWorker.computeHoliSheetImage)
        self.imageComputationThread.start()

        # Connect CommunicationChannel signals
        self._commChannel.sigUpdateImage.connect(self.update)

        # select detectors
        allDetectorNames = self._master.detectorsManager.getAllDeviceNames()

        try:
            if allDetectorNames[0].lower().find("light"):
                self.detectorLightsheetName = allDetectorNames[0]
                self.detectorHoloName = allDetectorNames[1]
            else:
                self.detectorLightsheetName = allDetectorNames[1]
                self.detectorHoloName = allDetectorNames[0]
        except Exception as e:
            self._logger.debug("No camera found - in debug mode?")

        # get all Lasers
        self.lasers = self._master.lasersManager.getAllDeviceNames()
        self.laser = self.lasers[0]
        try:
            self._master.lasersManager[self.laser].setGalvo(channel=1, frequency=10, offset=0, amplitude=1, clk_div=0, phase=0, invert=1, timeout=1)
        except  Exception as e:
            self._logger.error(e)

        # connect camera and stage
        #self.camera = self._setupInfo.autofocus.camera
        #self._master.detectorsManager[self.camera].startAcquisition()
        self.positionerName = self._master.positionersManager.getAllDeviceNames()[0]
        self.positioner = self._master.positionersManager[self.positionerName]
        self.imageComputationWorker.setPositioner(self.positioner)

        # Connect HoliSheetWidget signals
        if self._widget is not None:
            self._widget.sigShowToggled.connect(self.setShowHoliSheet)
            self._widget.sigPIDToggled.connect(self.setPID)
            self._widget.sigUpdateRateChanged.connect(self.changeRate)
            self._widget.sigSliderFocusValueChanged.connect(self.valueFocusChanged)
            self._widget.sigSliderPumpSpeedValueChanged.connect(self.valuePumpSpeedChanged)
            self._widget.sigSliderRotationSpeedValueChanged.connect(self.valueRotationSpeedChanged)
            self._widget.sigToggleLightsheet.connect(self.toggleLightsheet)
            # Connect buttons
            self._widget.snapRotationButton.clicked.connect(self.captureFullRotation)

        self.changeRate(self._widget.getUpdateRate())
        self.setShowHoliSheet(self._widget.getShowHoliSheetChecked())
        #self.setPID(self._widget.getPIDChecked())

        # start measurment thread (pressure)
        self.startTime = time.time()

    def toggleLightsheet(self, enabled):
        """ Toggle lightsheet. """
        if enabled:
            self._master.lasersManager[self.laser].setGalvo(channel=1, frequency=10, offset=0, amplitude=1, clk_div=2, phase=0, invert=1, timeout=1)
        else:
            self._master.lasersManager[self.laser].setGalvo(channel=1, frequency=0, offset=0, amplitude=1, clk_div=0, phase=0, invert=1, timeout=1)


    def valueFocusChanged(self, magnitude):
        """ Change magnitude. """
        self.dz = magnitude*1e-3
        self.imageComputationWorker.set_dz(self.dz)

    def valuePumpSpeedChanged(self, value):
        """ Change magnitude. """
        self.controlTarget = int(value)

        # we actually set the target value with this slider
        self._widget.updatePumpSpeed(self.controlTarget)
        if self.PIDenabled:
            self.positioner.setupPIDcontroller(PIDactive=self.PIDenabled , Kp=self.Kp, Ki=self.Ki, Kd=self.Kd, target=self.controlTarget, PID_updaterate=200)
        # Motor speed will be carried out automatically on the board
        #self.positioner.moveForever(speed=(self.speedPump,self.speedRotation,0),is_stop=False)
        #self.positioner.moveForever(speed=(self.speedPump,self.speedRotation,0),is_stop=False)

    def valueRotationSpeedChanged(self, value):
        """ Change magnitude. """
        self.speedRotation = int(value)
        self._widget.updateRotationSpeed(self.speedPump)
        self.tRoundtripRotation = self.stepsPerRotation/(0.001+self.speedRotation) # in s
        self.positioner.moveForever(speed=(self.speedPump,self.speedRotation,0),is_stop=False)

    def __del__(self):
        self.imageComputationThread.quit()
        self.imageComputationThread.wait()
        self.is_measure=False
        self.measurementThread.quit()
        if hasattr(super(), '__del__'):
            super().__del__()

    def setShowHoliSheet(self, enabled):
        """ Show or hide HoliSheet. """
        self.pixelsize = self._widget.getPixelSize()
        self.mWavelength = self._widget.getWvl()
        self.NA = self._widget.getNA()
        self.k0 = 2 * np.pi / (self.mWavelength)
        self.active = enabled
        self.init = False

    def setPID(self, enabled):
        """ Show or hide HoliSheet. """
        self.PIDenabled = enabled
        self.positioner.setupPIDcontroller(PIDactive=self.PIDenabled , Kp=self.Kp, Ki=self.Ki, Kd=self.Kd, target=self.controlTarget, PID_updaterate=200)

    def captureFullRotation(self):
        # TODO: Here we want to capture frames and display that in Napari?
        # TODO: better do recording not single frame acquisition?
        tstart = time.time()
        self.framesRoundtrip = []
        camera = self._master.detectorsManager[self.detectorLightsheetName]
        while((time.time()-tstart)<self.tRoundtripRotation):
            self.framesRoundtrip.append(camera.getLatestFrame())
        return self.framesRoundtrip # after that comes image procesing - how?

    def displayImage(self, im):
        """ Displays the image in the view. """
        self._widget.setImage(im)

    def changeRate(self, updateRate):
        """ Change update rate. """
        self.updateRate = updateRate
        self.it = 0

    def update(self, detectorName, im, init, isCurrentDetector):
        """ Update with new detector frame. """
        if not isCurrentDetector or not self.active:
            return

        if self.it == self.updateRate:
            self.it = 0
            self.imageComputationWorker.prepareForNewImage(im)
            self.sigImageReceived.emit()
        else:
            self.it += 1

    def updateSetPointData(self):
        if self.currPoint < self.buffer:
            self.setPointData[self.currPoint,0] = self.pressureValue
            self.setPointData[self.currPoint,1] = self.controlTarget

            self.timeData[self.currPoint] = time.time() - self.startTime
        else:
            self.setPointData[:-1,0] = self.setPointData[1:,0]
            self.setPointData[-1,0] = self.pressureValue
            self.setPointData[:-1,1] = self.setPointData[1:,1]
            self.setPointData[-1,1] = self.controlTarget
            self.timeData[:-1] = self.timeData[1:]
            self.timeData[-1] = time.time() - self.startTime
        self.currPoint += 1

    def updateMeasurements(self):
        self.pressureValue  = self.imageComputationWorker.grabMeasurement()
        self._widget.updatePumpPressure(self.pressureValue)
        # update plot
        self.updateSetPointData()
        if self.currPoint < self.buffer:
            self._widget.pressurePlotCurve.setData(self.timeData[1:self.currPoint],
                                                self.setPointData[1:self.currPoint,0])
        else:
            self._widget.pressurePlotCurve.setData(self.timeData, self.setPointData[:,0])

    class HoliSheetImageComputationWorker(Worker):
        sigHoliSheetImageComputed = Signal(np.ndarray)

        def __init__(self):
            super().__init__()

            self._logger = initLogger(self, tryInheritParent=False)
            self._numQueuedImages = 0
            self._numQueuedImagesMutex = Mutex()
            self.PSFpara = None
            self.pixelsize = 1
            self.dz = 1
            self.positioner = None
            self.pressureValue = 0

        def setPositioner(self, positioner):
            self.positioner = positioner

        def reconHoliSheet(self, image, PSFpara, N_subroi=1024, pixelsize=1e-3, dz=50e-3):
            mimage = nip.image(np.sqrt(image))
            mimage = nip.extract(mimage, [N_subroi,N_subroi])
            mimage.pixelsize=(pixelsize, pixelsize)
            mpupil = nip.ft(mimage)
            #nip.__make_propagator__(mpupil, PSFpara, doDampPupil=True, shape=mpupil.shape, distZ=dz)
            cos_alpha, sin_alpha = nip.cosSinAlpha(mimage, PSFpara)
            defocus = self.dz #  defocus factor
            PhaseMap = nip.defocusPhase(cos_alpha, defocus, PSFpara)
            propagated = nip.ft2d((np.exp(1j * PhaseMap))*mpupil)
            return np.squeeze(propagated)

        def computeHoliSheetImage(self):
            """ Compute HoliSheet of an image. """
            try:
                if self._numQueuedImages > 1:
                    return  # Skip this frame in order to catch up
                HoliSheetrecon = np.flip(np.abs(self.reconHoliSheet(self._image, PSFpara=self.PSFpara, N_subroi=1024, pixelsize=self.pixelsize, dz=self.dz)),1)

                self.sigHoliSheetImageComputed.emit(np.array(HoliSheetrecon))
            finally:
                self._numQueuedImagesMutex.lock()
                self._numQueuedImages -= 1
                self._numQueuedImagesMutex.unlock()

        def sigHoliSheetImageComputed(self, image):
            """ Must always be called before the worker receives a new image. """
            self._image = image
            self._numQueuedImagesMutex.lock()
            self._numQueuedImages += 1
            self._numQueuedImagesMutex.unlock()

        def set_dz(self, dz):
            self.dz = dz

        def set_PSFpara(self, PSFpara):
            self.PSFpara = PSFpara

        def set_pixelsize(self, pixelsize):
            self.pixelsize = pixelsize

        def grabMeasurement(self):
            try:
                self.pressureValue  = self.positioner.measure(sensorID=0)
            except Exception as e:
                self._logger.error(e)
            return self.pressureValue




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
