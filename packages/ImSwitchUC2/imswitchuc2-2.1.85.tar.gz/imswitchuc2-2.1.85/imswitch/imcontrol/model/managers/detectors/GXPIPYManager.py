import numpy as np

from imswitch.imcommon.model import initLogger
from .DetectorManager import DetectorManager, DetectorAction, DetectorNumberParameter, DetectorListParameter, DetectorBooleanParameter


class GXPIPYManager(DetectorManager):
    """ DetectorManager that deals with TheImagingSource cameras and the
    parameters for frame extraction from them.

    Manager properties:

    - ``cameraListIndex`` -- the camera's index in the Allied Vision camera list (list
      indexing starts at 0); set this string to an invalid value, e.g. the
      string "mock" to load a mocker
    - ``av`` -- dictionary of Allied Vision camera properties
    """

    def __init__(self, detectorInfo, name, **_lowLevelManagers):
        self.__logger = initLogger(self, instanceName=name)
        self.detectorInfo = detectorInfo

        try:
            self.binningValue = detectorInfo.managerProperties['gxipycam']["binning"]
           # we want a possibility to flatfield here
        except:
            self.binningValue = 1

        try:
            self.cameraId = detectorInfo.managerProperties['cameraListIndex']
        except:
            self.cameraId = 1

        try:
            pixelSize = detectorInfo.managerProperties['cameraEffPixelsize'] # mum
        except:
            # returning back to default pixelsize
            pixelSize = 1

        try:
            self.flipX = detectorInfo.managerProperties['gxipycam']['flipX']
        except:
            self.flipX = False

        try:
            self.flipY = detectorInfo.managerProperties['gxipycam']['flipY']
        except:
            self.flipY = False


        try:
            isRGB = detectorInfo.managerProperties['isRGB']
        except:
            isRGB = False

        self.flipImage = (self.flipX, self.flipY)

        self._camera = self._getGXObj(self.cameraId, self.binningValue, self.flipImage, isRGB)

        fullShape = (self._camera.SensorWidth,
                self._camera.SensorHeight)

        model = self._camera.model
        self._running = False
        self._adjustingParameters = False

        # Prepare parameters
        parameters = {
            'exposure': DetectorNumberParameter(group='Misc', value=1, valueUnits='ms',
                                                editable=True),
            'exposure_mode': DetectorListParameter(group='Misc',
                            value='manual',
                            options=['manual', 'auto', 'once'],
                            editable=True),
            'mode': DetectorBooleanParameter(group='Misc', value=name, editable=False), # auto or manual exposure settings
            'gain': DetectorNumberParameter(group='Misc', value=5, valueUnits='arb.u.',
                                            editable=True),
            'blacklevel': DetectorNumberParameter(group='Misc', value=0, valueUnits='arb.u.',
                                            editable=True),
            'binning': DetectorNumberParameter(group='Misc', value=1, valueUnits='arb.u.',
                                               editable=True),
            'image_width': DetectorNumberParameter(group='Misc', value=fullShape[0], valueUnits='arb.u.',
                        editable=False),
            'image_height': DetectorNumberParameter(group='Misc', value=fullShape[1], valueUnits='arb.u.',
                        editable=False),
            'frame_rate': DetectorNumberParameter(group='Misc', value=-1, valueUnits='fps',
                                    editable=True),
            'flat_fielding': DetectorBooleanParameter(group='Misc', value=True, editable=True),
            'binning': DetectorNumberParameter(group="Misc", value=1, valueUnits="arb.u.", editable=True),
            'flipX': DetectorBooleanParameter(group="Misc", value=self.flipX, editable=True),
            'flipY': DetectorBooleanParameter(group="Misc", value=self.flipY, editable=True),
            'trigger_source': DetectorListParameter(group='Acquisition mode',
                            value='Continuous',
                            options=['Continuous',
                                        'Internal trigger',
                                        'External trigger'],
                            editable=True),
            'Camera pixel size': DetectorNumberParameter(group='Miscellaneous', value=pixelSize,
                                                valueUnits='µm', editable=True)

            }

        # reading parameters from disk and write them to camrea
        for propertyName, propertyValue in detectorInfo.managerProperties['gxipycam'].items():
            self._camera.setPropertyValue(propertyName, propertyValue)
            parameters[propertyName].value = propertyValue



        # TODO: Not implemented yet
        self.crop(hpos=0, vpos=0, hsize=fullShape[0], vsize=fullShape[1])

        # Prepare actions
        actions = {
            'More properties': DetectorAction(group='Misc',
                                              func=self._camera.openPropertiesGUI)
        }

        super().__init__(detectorInfo, name, fullShape=fullShape, supportedBinnings=[1],
                         model=model, parameters=parameters, actions=actions, croppable=True)


    def _updatePropertiesFromCamera(self):
        self.setParameter('Real exposure time', self._camera.getPropertyValue('exposure_time')[0])
        self.setParameter('Internal frame interval',
                          self._camera.getPropertyValue('internal_frame_interval')[0])
        self.setParameter('Binning', self._camera.getPropertyValue('binning')[0])
        self.setParameter('Readout time', self._camera.getPropertyValue('timing_readout_time')[0])
        self.setParameter('Internal frame rate',
                          self._camera.getPropertyValue('internal_frame_rate')[0])

        triggerSource = self._camera.getPropertyValue('trigger_source')
        if triggerSource == 1:
            self.setParameter('Trigger source', 'Internal trigger')
        else:
            triggerMode = self._camera.getPropertyValue('trigger_mode')
            if triggerSource == 2 and triggerMode == 6:
                self.setParameter('Trigger source', 'External "start-trigger"')
            elif triggerSource == 2 and triggerMode == 1:
                self.setParameter('Trigger source', 'External "frame-trigger"')

    def getLatestFrame(self, is_save=None, is_resize=True, returnFrameNumber=False):
        if returnFrameNumber:
            frame, frameNumber = self._camera.getLast(returnFrameNumber=returnFrameNumber)
            return frame, frameNumber
        else:
            frame = self._camera.getLast(returnFrameNumber=returnFrameNumber)
            return frame

    def setParameter(self, name, value):
        """Sets a parameter value and returns the value.
        If the parameter doesn't exist, i.e. the parameters field doesn't
        contain a key with the specified parameter name, an error will be
        raised."""

        super().setParameter(name, value)

        if name not in self._DetectorManager__parameters:
            raise AttributeError(f'Non-existent parameter "{name}" specified')

        value = self._camera.setPropertyValue(name, value)
        return value

    def getParameter(self, name):
        """Gets a parameter value and returns the value.
        If the parameter doesn't exist, i.e. the parameters field doesn't
        contain a key with the specified parameter name, an error will be
        raised."""

        if name not in self._DetectorManager__parameters:
            raise AttributeError(f'Non-existent parameter "{name}" specified')

        value = self._camera.getPropertyValue(name)
        return value


    def setTriggerSource(self, source):
        """Set trigger source using the improved camera interface.""" 
        try:
            if source in ['Continuous', 'Continous']:  # Handle both old and new spellings
                self._performSafeCameraAction(
                    lambda: self._camera.setTriggerSource('Continuous')
                )
            elif source == 'Internal trigger':
                self._performSafeCameraAction(
                    lambda: self._camera.setTriggerSource('Internal trigger')
                )
            elif source == 'External trigger':
                self._performSafeCameraAction(
                    lambda: self._camera.setTriggerSource('External trigger')
                )
            else:
                raise ValueError(f'Invalid trigger source "{source}"')
        except Exception as e:
            self.__logger.error(f'Failed to set trigger source to {source}: {e}')


    def getChunk(self):
        try:
            return self._camera.getLastChunk()
        except:
            return None

    def sendSoftwareTrigger(self):
        """Send software trigger pulse."""
        try:
            return self._camera.sendSoftwareTrigger()
        except Exception as e:
            self.__logger.error(f'Failed to send software trigger: {e}')
            return False

    def flushBuffers(self):
        self._camera.flushBuffer()

    def startAcquisition(self, liveView=False):
        if self._camera.model == "mock":

            # reconnect? Not sure if this is smart..
            del self._camera
            self._camera = self._getGXObj(self.cameraId, self.binningValue)

            for propertyName, propertyValue in self.detectorInfo.managerProperties['gxipycam'].items():
                self._camera.setPropertyValue(propertyName, propertyValue)

            fullShape = (self._camera.SensorWidth,
                        self._camera.SensorHeight)

            model = self._camera.model
            self._running = False
            self._adjustingParameters = False

            # TODO: Not implemented yet
            self.crop(hpos=0, vpos=0, hsize=fullShape[0], vsize=fullShape[1])

        if not self._running:
            self._camera.start_live()
            self._running = True
            self.__logger.debug('startlive')

    def stopAcquisition(self):
        if self._running:
            self._running = False
            self._camera.suspend_live()
            self.__logger.debug('suspendlive')

    def stopAcquisitionForROIChange(self):
        self._running = False
        self._camera.stop_live()
        self.__logger.debug('stoplive')

    def finalize(self) -> None:
        super().finalize()
        self.__logger.debug('Safely disconnecting the camera...')
        self._camera.close()

    @property
    def pixelSizeUm(self):
        umxpx = self.parameters['Camera pixel size'].value
        return [1, umxpx, umxpx]

    def setPixelSizeUm(self, pixelSizeUm):
        self.parameters['Camera pixel size'].value = pixelSizeUm

    def crop(self, hpos, vpos, hsize, vsize):
        '''
        hpos - horizontal start position of crop window
        vpos - vertical start position of crop window
        hsize - horizontal size of crop window
        vsize - vertical size of crop window
        '''
        def cropAction():
            self.__logger.debug(
                f'{self._camera.model}: crop frame to {hsize}x{vsize} at {hpos},{vpos}.'
            )
            self._camera.setROI(hpos, vpos, hsize, vsize)
            # TOdO: weird hackaround
            self._shape = (self._camera.camera.Width.get()//self._camera.binning, self._camera.camera.Height.get()//self._camera.binning)
            self._frameStart = (hpos, vpos)
            pass
        try:
            self._performSafeCameraAction(cropAction)
        except Exception as e:
            self.__logger.error(e)
            # TODO: unsure if frameStart is needed? Try without.
        # This should be the only place where self.frameStart is changed

        # Only place self.shapes is changed

        pass

    def _performSafeCameraAction(self, function):
        """ This method is used to change those camera properties that need
        the camera to be idle to be able to be adjusted.
        """
        self._adjustingParameters = True
        wasrunning = self._running
        self.stopAcquisitionForROIChange()
        function()
        if wasrunning:
            self.startAcquisition()
        self._adjustingParameters = False

    def openPropertiesDialog(self):
        self._camera.openPropertiesGUI()

    def _getGXObj(self, cameraId, binning=1, flipImage=(False, False), isRGB=False):
        try:
            import os
            if os.name == 'darwin':
                from imswitch.imcontrol.model.interfaces.tiscamera_mock import MockCameraTIS
                camera = MockCameraTIS()
            else:
                from imswitch.imcontrol.model.interfaces.gxipycamera import CameraGXIPY
                self.__logger.debug(f'Trying to initialize Daheng Imaging camera {cameraId}')
                camera = CameraGXIPY(cameraNo=cameraId, binning=binning, flipImage=flipImage, isRGB=isRGB)
        except Exception as e:
            self.__logger.debug(e)
            self.__logger.warning(f'Failed to initialize CameraGXIPY {cameraId}, loading TIS mocker')
            from imswitch.imcontrol.model.interfaces.tiscamera_mock import MockCameraTIS
            camera = MockCameraTIS()

        self.__logger.info(f'Initialized camera, model: {camera.model}')
        return camera

    def getFrameNumber(self):
        return self._camera.getFrameNumber()

    def closeEvent(self):
        self._camera.close()

    def recordFlatfieldImage(self):
        '''
        record n images and average them before subtracting from the latest frame
        '''
        self._camera.recordFlatfieldImage()

# Copyright (C) ImSwitch developers 2021
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
