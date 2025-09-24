from imswitch.imcommon.model import initLogger, ostools
import numpy as np
import time
import threading
from imswitch import IS_HEADLESS
from scipy.ndimage import gaussian_filter
from collections import deque

from imswitch.imcommon.model import dirtools, initLogger, APIExport
from ..basecontrollers import ImConWidgetController
from imswitch.imcommon.framework import Signal, Thread, Worker, Mutex, Timer
from ..basecontrollers import LiveUpdatedController


class FlatfieldController(LiveUpdatedController):
    """Linked to FlatfieldWidget."""
    sigImageReceived = Signal()


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._logger = initLogger(self)

        self.flatfieldTask = None
        self.flatfieldStack = np.ones((1,1,1))

        if not IS_HEADLESS:
            self._widget.startButton.clicked.connect(self.startflatfield)
            self._widget.stopButton.clicked.connect(self.stopflatfield)

        # select detectors
        allDetectorNames = self._master.detectorsManager.getAllDeviceNames()
        self.detector = self._master.detectorsManager[allDetectorNames[0]]
        self.isflatfieldRunning = False
        self.sigImageReceived.connect(self.displayImage)
        # select stage
        self.stages = self._master.positionersManager[self._master.positionersManager.getAllDeviceNames()[0]]

    def goToPosition(self, posX, posY):
        self.stages.move(value=(posX,posY), axis="XY", is_absolute=True, is_blocking=True, acceleration=(100000,100000))

    def displayImage(self):
        # a bit weird, but we cannot update outside the main thread
        name = self.histoScanStackName
        # subsample stack
        isRGB = self.flatfieldStack.shape[-1]==3
        if isRGB:
            img = np.uint8(self.flatfieldStack*255)
        else:
            img = self.flatfieldStack
        self._widget.setImageNapari(img, colormap="gray", isRGB=isRGB, name=name, pixelsize=(1,1), translation=(0,0))

    def getNImagesToAverage(self):
        return np.int32(self.nImagesToAverageTextedit.text())

    def getMaxStepSize(self):
        return np.float32(self.maxStepsizeTextedit.text())

    def startflatfield(self):
        nImagesToTake = self._widget.getNImagesToAverage()
        maxStepSize = self._widget.getMaxStepSize()
        self._widget.startButton.setEnabled(False)
        self._widget.stopButton.setEnabled(True)
        self._widget.startButton.setText("Running")
        self._widget.stopButton.setText("Stop")
        self._widget.stopButton.setStyleSheet("background-color: red")
        self._widget.startButton.setStyleSheet("background-color: green")
        self.isflatfieldRunning = True
        self.flatfieldTask = threading.Thread(target=self.flatfieldThread, args=(nImagesToTake, maxStepSize))
        self.flatfieldTask.start()

    def stopflatfield(self):
        self.isflatfieldRunning = False
        self._widget.startButton.setEnabled(True)
        self._widget.stopButton.setEnabled(False)
        self._widget.startButton.setText("Start")
        self._widget.stopButton.setText("Stopped")
        self._widget.stopButton.setStyleSheet("background-color: gray")
        self._widget.startButton.setStyleSheet("background-color: gray")

    def flatfieldThread(self, nImagesToTake, maxStepSize):
        self._logger.debug("flatfield thread started.")

        initialPosition = self.stages.getPosition()
        gaussKernelSize = self._widget.getGaussKernelSize()
        initPosX = initialPosition["X"]
        initPosY = initialPosition["Y"]
        if not self.detector._running: self.detector.startAcquisition()

        # move to n positions with maximum step size in xy and take nImagesToTake images, sum them and create a flatfield image
        flatfieldStack = []
        for iPosition in range(nImagesToTake):
            if not self.isflatfieldRunning:
                break
            posX = initPosX + np.random.uniform(-maxStepSize, maxStepSize)
            posY = initPosY + np.random.uniform(-maxStepSize, maxStepSize)
            self.goToPosition(posX, posY)
            time.sleep(0.1)
            im = self.detector.getLatestFrame()
            flatfieldStack.append(im)
        # now compute the mean and do a gaussian blur
        flatfieldStack = np.mean(np.array(flatfieldStack), axis=0)
        flatfieldStack = gaussian_filter(flatfieldStack, sigma=gaussKernelSize)
        flatfieldStack = flatfieldStack/np.max(flatfieldStack)

        self._logger.debug("flatfield thread finished.")

        # move to initial position
        self.goToPosition(initPosX, initPosY)

        # cleanup and change button state
        self._widget.startButton.setEnabled(True)
        self._widget.stopButton.setEnabled(False)
        self._widget.startButton.setText("Start")
        self._widget.stopButton.setText("Stopped")
        self._widget.stopButton.setStyleSheet("background-color: gray")
        self._widget.startButton.setStyleSheet("background-color: gray")
        self.isflatfieldRunning = False

        # display result in napari - need to add this to the camera controller..
        self.histoScanStackName = "Flatfield Stack"
        self.flatfieldStack = flatfieldStack

        # set flatfield image in detector
        try:
            #self.detector.setFlatfieldImage(np.squeeze(self.flatfieldStack), True)
            self._master.FlatfieldManager.setFlatfieldImage(self.flatfieldStack)
            # check if self._master has a class FlatfieldManager
        except Exception as e:
            self._logger.error("Could not set flatfield image.")
            self._logger.error(e)
        self.sigImageReceived.emit()
