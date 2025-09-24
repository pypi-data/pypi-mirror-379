import numpy as np

from imswitch.imcommon.model import initLogger
from .DetectorManager import DetectorManager, DetectorAction, DetectorNumberParameter, DetectorListParameter


class ThorCamSciManager(DetectorManager):
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
            self.binningValue = detectorInfo.managerProperties['thorcamsci']["binning"]
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


        self._camera = self._getThorCamSci(self.cameraId, self.binningValue)

        fullShape = (self._camera.SensorWidth,
                self._camera.SensorHeight)

        model = self._camera.model
        self._running = False
        self._adjustingParameters = False

        # Prepare parameters
        parameters = {
            'exposure': DetectorNumberParameter(group='Misc', value=1, valueUnits='ms',
                                                editable=True),
            'gain': DetectorNumberParameter(group='Misc', value=0, valueUnits='arb.u.',
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
            'binning': DetectorNumberParameter(group="Misc", value=1, valueUnits="arb.u.", editable=True),
            'trigger_source': DetectorListParameter(group='Acquisition mode',
                            value='Continous',
                            options=['Continous',
                                        'Internal trigger',
                                        'External trigger'],
                            editable=True),
            'Camera pixel size': DetectorNumberParameter(group='Miscellaneous', value=pixelSize,
                                                valueUnits='µm', editable=True)
            }

        # reading parameters from disk and write them to camrea
        for propertyName, propertyValue in detectorInfo.managerProperties['thorcamsci'].items():
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

    def getLatestFrame(self, is_save=False):
        frame = self._camera.getLast()
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

        if name not in self._parameters:
            raise AttributeError(f'Non-existent parameter "{name}" specified')

        value = self._camera.getPropertyValue(name)
        return value


    def setTriggerSource(self, source):
        if source == 'Continous':
            self._performSafeCameraAction(
                lambda: self._camera.setPropertyValue('trigger_source', 0)
            )
        elif source == 'Internal trigger':
            self._performSafeCameraAction(
                lambda: self._camera.setPropertyValue('trigger_source', 1)
            )
        elif source == 'External trigger':
            self._performSafeCameraAction(
                lambda: self._camera.setPropertyValue('trigger_source', 2)
            )
        else:
            raise ValueError(f'Invalid trigger source "{source}"')


    def getChunk(self):
        try:
            return self._camera.getLastChunk()
        except:
            return None

    def flushBuffers(self):
        self._camera.flushBuffer()

    def startAcquisition(self, liveView=False):
        if self._camera.model == "mock":

            # reconnect? Not sure if this is smart..
            del self._camera
            self._camera = self._getThorCamSci(self.cameraId, self.binningValue)

            for propertyName, propertyValue in self.detectorInfo.managerProperties['thorcamsci'].items():
                self._camera.setPropertyValue(propertyName, propertyValue)

            fullShape = (self._camera.SensorWidth,
                        self._camera.SensorHeight)

            model = self._camera.model
            self._running = False
            self._adjustingParameters = False

            # TODO: Not implemented yet
            self.crop(hpos=0, vpos=0, hsize=fullShape[0], vsize=fullShape[1])


            # Prepare parameters
            parameters = {
                'exposure': DetectorNumberParameter(group='Misc', value=100, valueUnits='ms',
                                                    editable=True),
                'gain': DetectorNumberParameter(group='Misc', value=1, valueUnits='arb.u.',
                                                editable=True),
                'blacklevel': DetectorNumberParameter(group='Misc', value=100, valueUnits='arb.u.',
                                                editable=True),
                'image_width': DetectorNumberParameter(group='Misc', value=fullShape[0], valueUnits='arb.u.',
                            editable=False),
                'image_height': DetectorNumberParameter(group='Misc', value=fullShape[1], valueUnits='arb.u.',
                            editable=False),
                'frame_rate': DetectorNumberParameter(group='Misc', value=-1, valueUnits='fps',
                                        editable=True),
                'trigger_source': DetectorListParameter(group='Acquisition mode',
                                value='Continous',
                                options=['Continous',
                                            'Internal trigger',
                                            'External trigger'],
                                editable=True),
                'pixelSize': DetectorNumberParameter(group='Miscellaneous', value=1,
                                                    valueUnits='µm', editable=True)
                }

            # Prepare actions
            actions = {
                'More properties': DetectorAction(group='Misc',
                                                func=self._camera.openPropertiesGUI)
            }

            #super().__init__(detectorInfo, name, fullShape=fullShape, supportedBinnings=[1],
            #               model=model, parameters=parameters, actions=actions, croppable=True)

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

        def cropAction():
            self.__logger.debug(
                f'{self._camera.model}: crop frame to {hsize}x{vsize} at {hpos},{vpos}.'
            )
        '''
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
        '''
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

    def _getThorCamSci(self, cameraId, binning=1):
        try:
            from imswitch.imcontrol.model.interfaces.thorcamscicamera import CameraThorCamSci
            self.__logger.debug(f'Trying to initialize Thorlabs Scientific camera {cameraId}')
            camera = CameraThorCamSci(cameraNo=cameraId, binning=binning)

        except Exception as e:
            self.__logger.debug(e)
            self.__logger.warning(f'Failed to initialize ThorCamSci {cameraId}, loading TIS mocker')
            from imswitch.imcontrol.model.interfaces.tiscamera_mock import MockCameraTIS
            camera = MockCameraTIS()

        self.__logger.info(f'Initialized camera, model: {camera.model}')
        return camera

    def getFrameNumber(self):
        return self._camera.getFrameNumber()

    def closeEvent(self):
        self._camera.close()

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
