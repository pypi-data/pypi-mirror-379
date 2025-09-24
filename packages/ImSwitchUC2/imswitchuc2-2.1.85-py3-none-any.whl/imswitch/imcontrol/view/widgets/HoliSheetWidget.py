import pyqtgraph as pg
from qtpy import QtCore, QtWidgets
import pyqtgraph as pg

from imswitch.imcommon.view.guitools import pyqtgraphtools
from imswitch.imcontrol.view import guitools
from .basewidgets import NapariHybridWidget


class HoliSheetWidget(NapariHybridWidget):
    """ Displays the HoliSheet transform of the image. """

    sigShowToggled = QtCore.Signal(bool)  # (enabled)
    sigPIDToggled = QtCore.Signal(bool)  # (enabled)
    sigUpdateRateChanged = QtCore.Signal(float)  # (rate)
    sigSliderFocusValueChanged = QtCore.Signal(float)  # (value)
    sigSliderPumpSpeedValueChanged = QtCore.Signal(float)  # (value)
    sigSliderRotationSpeedValueChanged = QtCore.Signal(float)  # (value)
    sigToggleLightsheet = QtCore.Signal(bool) # (enabled)

    def __post_init__(self):

        # Graphical elements
        self.showCheck = QtWidgets.QCheckBox('Show HoliSheet')
        self.showCheck.setCheckable(True)
        self.PIDCheck = QtWidgets.QCheckBox('Enable PID')
        self.PIDCheck.setCheckable(True)
        self.lineRate = QtWidgets.QLineEdit('0')
        self.labelRate = QtWidgets.QLabel('Update rate')
        self.wvlLabel = QtWidgets.QLabel('Wavelength [um]')
        self.wvlEdit = QtWidgets.QLineEdit('0.488')
        self.pixelSizeLabel = QtWidgets.QLabel('Pixel size [um]')
        self.pixelSizeEdit = QtWidgets.QLineEdit('3.45')
        self.naLabel = QtWidgets.QLabel('NA')
        self.naEdit = QtWidgets.QLineEdit('0.3')
        self.labelRotationSpeed = QtWidgets.QLabel('Speed Rotation')
        self.labelPumpSpeed = QtWidgets.QLabel('Speed Pump')
        self.labelPumpPressure = QtWidgets.QLabel('Pump Pressure')
        self.snapRotationButton = guitools.BetterPushButton('Snap Rotation')


        self.snapRotationButton.setCheckable(True)
        self.snapRotationButton.setSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                      QtWidgets.QSizePolicy.Expanding)


        # Slider to set the focus value
        valueDecimals = 1
        valueRange = (0,100)
        tickInterval = 5
        singleStep = 1
        self.sliderFocus = guitools.FloatSlider(QtCore.Qt.Horizontal, self, allowScrollChanges=False,
                                           decimals=valueDecimals)
        self.sliderFocus.setFocusPolicy(QtCore.Qt.NoFocus)
        valueRangeMin, valueRangeMax = valueRange

        self.sliderFocus.setMinimum(valueRangeMin)
        self.sliderFocus.setMaximum(valueRangeMax)
        self.sliderFocus.setTickInterval(tickInterval)
        self.sliderFocus.setSingleStep(singleStep)
        self.sliderFocus.setValue(0)

        # Slider to set the focus value
        valueDecimalsPump = 1
        valueRangePump = (300,700)
        tickIntervalPump = 1
        singleStepPump = 1
        self.sliderPumpSpeed = guitools.FloatSlider(QtCore.Qt.Horizontal, self, allowScrollChanges=False,
                                        decimals=valueDecimalsPump)
        self.sliderPumpSpeed.setFocusPolicy(QtCore.Qt.NoFocus)
        valueRangeMinPump, valueRangeMaxPump = valueRangePump

        self.sliderPumpSpeed.setMinimum(valueRangeMinPump)
        self.sliderPumpSpeed.setMaximum(valueRangeMaxPump)
        self.sliderPumpSpeed.setTickInterval(tickIntervalPump)
        self.sliderPumpSpeed.setSingleStep(singleStepPump)
        self.sliderPumpSpeed.setValue(500)

        # Slider to set the focus value
        valueDecimalsRotation = 1
        valueRangeRotation = (0,10000)
        tickIntervalRotation = 200
        singleStepRotation = 200
        self.sliderRotationSpeed = guitools.FloatSlider(QtCore.Qt.Horizontal, self, allowScrollChanges=False,
                                        decimals=valueDecimalsRotation)
        self.sliderRotationSpeed.setFocusPolicy(QtCore.Qt.NoFocus)
        valueRangeMinRotation, valueRangeMaxRotation = valueRangeRotation

        self.sliderRotationSpeed.setMinimum(valueRangeMinRotation)
        self.sliderRotationSpeed.setMaximum(valueRangeMaxRotation)
        self.sliderRotationSpeed.setTickInterval(tickIntervalRotation)
        self.sliderRotationSpeed.setSingleStep(singleStepRotation)
        self.sliderRotationSpeed.setValue(0)

        # Focus lock graph
        self.pressureSenseGraph = pg.GraphicsLayoutWidget()
        self.pressureSenseGraph.setAntialiasing(True)
        self.pressurePlot = self.pressureSenseGraph.addPlot(row=1, col=0)
        self.pressurePlot.setLabels(bottom=('Time', 's'), left=('Pressure', 'psi'))
        self.pressurePlot.showGrid(x=True, y=True)
        # update this (self.pressurePlotCurve.setData(X,Y)) with update(focusSignal) function
        self.pressurePlotCurve = self.pressurePlot.plot(pen='y')
        self.btnToggleLightsheet = QtWidgets.QPushButton('Toggle Lightsheet')
        self.btnToggleLightsheet.setCheckable(True)
        self.btnToggleLightsheet.setSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                        QtWidgets.QSizePolicy.Expanding)
        self.btnToggleLightsheet.clicked.connect(self.sigToggleLightsheet)

        # Add elements to GridLayout
        grid = QtWidgets.QGridLayout()
        self.setLayout(grid)
        grid.addWidget(self.wvlLabel, 0, 0, 1, 1)
        grid.addWidget(self.wvlEdit, 0, 1, 1, 1)
        grid.addWidget(self.pixelSizeLabel, 1, 0, 1, 1)
        grid.addWidget(self.pixelSizeEdit, 1, 1, 1, 1)
        grid.addWidget(self.naLabel, 2, 0, 1, 1)
        grid.addWidget(self.naEdit, 2, 1, 1, 1)
        grid.addWidget(self.showCheck, 3, 0, 1, 1)
        grid.addWidget(self.sliderFocus, 3, 1, 1, 1)
        grid.addWidget(self.labelPumpSpeed, 0, 2, 1, 1)
        grid.addWidget(self.sliderPumpSpeed, 0, 3, 1, 1)
        grid.addWidget(self.labelRotationSpeed, 1, 2, 1, 1)
        grid.addWidget(self.sliderRotationSpeed, 1, 3, 1, 1)
        grid.addWidget(self.snapRotationButton, 2, 2, 1, 1)
        grid.addWidget(self.labelPumpPressure, 2, 3, 1, 1)
        grid.addWidget(self.labelRate, 3, 2, 1, 1)
        grid.addWidget(self.lineRate, 3, 3, 1, 1)
        grid.addWidget(self.pressureSenseGraph, 4, 0, 1, 4)
        grid.addWidget(self.PIDCheck, 2, 3, 1, 1)
        grid.addWidget(self.btnToggleLightsheet, 4, 2, 1, 2)

        # grid.setRowMinimumHeight(0, 300)

        # Connect signals
        self.showCheck.toggled.connect(self.sigShowToggled)
        self.PIDCheck.toggled.connect(self.sigPIDToggled)
        self.sliderFocus.valueChanged.connect(
            lambda value: self.sigSliderFocusValueChanged.emit(value)
        )
        self.sliderPumpSpeed.valueChanged.connect(
            lambda value: self.sigSliderPumpSpeedValueChanged.emit(value)
        )
        self.sliderRotationSpeed.valueChanged.connect(
            lambda value: self.sigSliderRotationSpeedValueChanged.emit(value)
        )

        self.lineRate.textChanged.connect(
            lambda: self.sigUpdateRateChanged.emit(self.getUpdateRate())
        )
        self.layer = None

    def updatePumpSpeed(self, speed):
        self.labelPumpSpeed.setText(f'Speed Pump {speed} [stp"\"s]')

    def updatePumpPressure(self, pressure):
        self.labelPumpPressure.setText(f'Pump Pressure {"{0:.2f}".format(pressure)} [psi]')

    def updateRotationSpeed(self, speed):
        self.labelRotationSpeed.setText(f'Speed Rotation {speed} [stp"\"s]')

    def getWvl(self):
        return float(self.wvlEdit.text())

    def getPixelSize(self):
        return float(self.pixelSizeEdit.text())

    def getNA(self):
        return float(self.naEdit.text())

    def getShowHoliSheetChecked(self):
        return self.showCheck.isChecked()

    def getPIDChecked(self):
        return self.PIDCheck.isChecked()

    def getUpdateRate(self):
        return float(self.lineRate.text())

    def getImage(self):
        if self.layer is not None:
            return self.img.image

    def setImage(self, im):
        if self.layer is None or self.layer.name not in self.viewer.layers:
            self.layer = self.viewer.add_image(im, rgb=False, name="HoliSheet", blending='additive')
        self.layer.data = im


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
