import os
import cv2
import math
import time
from imswitch import IS_HEADLESS, __file__
import threading
import numpy as np
import matplotlib.pyplot as plt

from skimage.draw import line
from scipy.signal import convolve2d
from imswitch.imcommon.model import initLogger

try:
    import NanoImagingPack as nip

    IS_NIP = True
except:
    IS_NIP = False

# Makes sure code still executes without numba, albeit extremely slow
try:
    from numba import njit, prange
except ModuleNotFoundError:
    prange = range

    def njit(*args, **kwargs):
        def wrapper(func):
            return func

        return wrapper

"""
End-to-end astigmatism autofocus simulation:
- Simulated microscope with Z-scan, rotated astigmatism, and XY drift
- Rotation-invariant second-moment focus metric (fast, no fits)
- Plots + saves stack (NPZ) and metrics (CSV)
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from math import cos, sin

# ----------------------- Simulation -----------------------

class AstigmaticMicroscopeSimulator:
    def __init__(
        self,
        H=128,
        W=128,
        roi_half=28,
        phi_deg=33.0,      # astig axis rotation w.r.t. camera x
        s0=1.7,            # base sigma at nominal focus (px)
        astig_slope=0.33,  # sigma_x = s0 + a*z, sigma_y = s0 - a*z
        amp=2400.0,
        bg=35.0,
        read_noise=0*2.2,
        poisson=0*True,
        seed=7,
    ):
        self.H, self.W = H, W
        self.roi_half = roi_half
        self.phi = np.deg2rad(phi_deg)
        self.s0 = float(s0)
        self.a = float(astig_slope)
        self.amp = float(amp)
        self.bg = float(bg)
        self.read_noise = float(read_noise)
        self.poisson = bool(poisson)
        self.rng = np.random.default_rng(seed)

        y, x = np.mgrid[0:H, 0:W].astype(np.float32)
        self.xgrid = x
        self.ygrid = y

        # ROI indices (fixed crop around center; centroiding handles drift)
        cx = W // 2
        cy = H // 2
        r = roi_half
        self.roi_slice = np.s_[cy - r : cy + r, cx - r : cx + r]

    def xy_drift(self, z):
        # linear + sinusoidal drift to stress-test the metric
        dx = 0.25 * z + 1.2 * np.sin(0.8 * z)
        dy = -0.18 * z + 1.0 * np.cos(0.6 * z)
        return dx, dy

    def render_frame(self, z):
        x, y = self.xgrid, self.ygrid
        dx, dy = self.xy_drift(z)
        cx = self.W / 2 + dx
        cy = self.H / 2 + dy

        sx = max(self.s0 + self.a * z, 0.5)
        sy = max(self.s0 - self.a * z, 0.5)

        # rotate coords by phi (principal axes of astigmatism)
        xp = (x - cx) * cos(self.phi) + (y - cy) * sin(self.phi)
        yp = -(x - cx) * sin(self.phi) + (y - cy) * cos(self.phi)

        g = np.exp(-0.5 * ((xp / sx) ** 2 + (yp / sy) ** 2))
        I = self.amp * g + self.bg

        if self.poisson:
            I = self.rng.poisson(I).astype(np.float32)
        else:
            I = I.astype(np.float32)

        I += self.rng.normal(0, self.read_noise, I.shape).astype(np.float32)
        return np.clip(I, 0, None)



class VirtualMicroscopeManager:
    """A low-level wrapper for TCP-IP communication (ESP32 REST API)
       with added objective control that toggles the objective lens.
       Toggling the objective will double the image magnification by
       binning the pixels (2x2 binning).
    """

    def __init__(self, rs232Info, name, **_lowLevelManagers):
        self.__logger = initLogger(self, instanceName=name)
        self._settings = rs232Info.managerProperties
        self._name = name

        try:
            self._imagePath = rs232Info.managerProperties["imagePath"]
            if self._imagePath not in ["simplant", "smlm", "astigmatism"]:
                raise NameError
        except:
            package_dir = os.path.dirname(os.path.abspath(__file__))
            self._imagePath = os.path.join(
                package_dir, "_data/images/histoASHLARStitch.jpg"
            )
            self.__logger.info(
                "If you want to use the plant, use 'imagePath': 'simplant', 'astigmatism' in your setup.json"
            )

        self._virtualMicroscope = VirtualMicroscopy(self._imagePath)
        self._positioner = self._virtualMicroscope.positioner
        self._camera = self._virtualMicroscope.camera
        self._illuminator = self._virtualMicroscope.illuminator
        self._objective = self._virtualMicroscope.objective

        # Initialize objective state: 1 (default) => no binning, 2 => binned image (2x magnification)
        self.currentObjective = 1
        self._camera.binning = False

    def toggleObjective(self):
        """
        Toggle the objective lens.
        When toggled, the virtual objective move is simulated,
        and the image magnification is changed by binning the pixels.
        """
        if self.currentObjective == 1:
            # Move to objective 2: simulate move and apply 2x binning
            self.__logger.info("Switching to Objective 2: Applying 2x binning")
            # Here one could call a REST API endpoint like:
            # /ObjectiveController/moveToObjective?slot=2
            self.currentObjective = 2
            self._camera.binning = True
        else:
            # Move back to objective 1: remove binning
            self.__logger.info("Switching to Objective 1: Removing binning")
            # Here one could call a REST API endpoint like:
            # /ObjectiveController/moveToObjective?slot=1
            self.currentObjective = 1
            self._camera.binning = False

    def finalize(self):
        self._virtualMicroscope.stop()



class Positioner:
    def __init__(self, parent):
        self._parent = parent
        self.position = {"X": 0, "Y": 0, "Z": 0, "A": 0}
        self.mDimensions = (self._parent.camera.SensorHeight, self._parent.camera.SensorWidth)
        self.lock = threading.Lock()
        if IS_NIP:
            self.psf = self.compute_psf(dz=0)
        else:
            self.psf = None

    def move(self, x=None, y=None, z=None, a=None, is_absolute=False):
        with self.lock:
            if is_absolute:
                if x is not None:
                    self.position["X"] = x
                if y is not None:
                    self.position["Y"] = y
                if z is not None:
                    self.position["Z"] = z
                    self.compute_psf(self.position["Z"])
                if a is not None:
                    self.position["A"] = a
            else:
                if x is not None:
                    self.position["X"] += x
                if y is not None:
                    self.position["Y"] += y
                if z is not None:
                    self.position["Z"] += z
                    self.compute_psf(self.position["Z"])
                if a is not None:
                    self.position["A"] += a

    def get_position(self):
        with self.lock:
            return self.position.copy()

    def compute_psf(self, dz):
        dz = np.float32(dz)
        print("Defocus:" + str(dz))
        if IS_NIP and dz != 0:
            obj = nip.image(np.zeros(self.mDimensions))
            obj.pixelsize = (100.0, 100.0)
            paraAbber = nip.PSF_PARAMS()
            paraAbber.aberration_types = [paraAbber.aberration_zernikes.spheric]
            paraAbber.aberration_strength = [np.float32(dz) / 10]
            psf = nip.psf(obj, paraAbber)
            self.psf = psf.copy()
            del psf
            del obj
        else:
            self.psf = None

    def get_psf(self):
        return self.psf


class Illuminator:
    def __init__(self, parent):
        self._parent = parent
        self.intensity = 0
        self.lock = threading.Lock()

    def set_intensity(self, channel=1, intensity=0):
        with self.lock:
            self.intensity = intensity

    def get_intensity(self, channel):
        with self.lock:
            return self.intensity


class VirtualMicroscopy:
    def __init__(self, filePath="path_to_image.jpeg"):
        self.camera = Camera(self, filePath)
        self.positioner = Positioner(self)
        self.illuminator = Illuminator(self)
        self.objective = Objective(self)

    def stop(self):
        pass


@njit(parallel=True)
def FromLoc2Image_MultiThreaded(
    xc_array: np.ndarray, yc_array: np.ndarray, photon_array: np.ndarray,
    sigma_array: np.ndarray, image_height: int, image_width: int, pixel_size: float
):
    Image = np.zeros((image_height, image_width))
    for ij in prange(image_height * image_width):
        j = int(ij / image_width)
        i = ij - j * image_width
        for xc, yc, photon, sigma in zip(xc_array, yc_array, photon_array, sigma_array):
            if (photon > 0) and (sigma > 0):
                S = sigma * math.sqrt(2)
                x = i * pixel_size - xc
                y = j * pixel_size - yc
                if (x + pixel_size / 2) ** 2 + (y + pixel_size / 2) ** 2 < 16 * sigma**2:
                    ErfX = math.erf((x + pixel_size) / S) - math.erf(x / S)
                    ErfY = math.erf((y + pixel_size) / S) - math.erf(y / S)
                    Image[j][i] += 0.25 * photon * ErfX * ErfY
    return Image


def binary2locs(img: np.ndarray, density: float):
    all_locs = np.nonzero(img == 1)
    n_points = int(len(all_locs[0]) * density)
    selected_idx = np.random.choice(len(all_locs[0]), n_points, replace=False)
    filtered_locs = all_locs[0][selected_idx], all_locs[1][selected_idx]
    return filtered_locs


def createBranchingTree(width=5000, height=5000, lineWidth=3):
    np.random.seed(0)
    image = np.ones((height, width), dtype=np.uint8) * 255

    def draw_vessel(start, end, image):
        rr, cc = line(start[0], start[1], end[0], end[1])
        try:
            image[rr, cc] = 0
        except:
            return

    def draw_tree(start, angle, length, depth, image, reducer, max_angle=40):
        if depth == 0:
            return
        end = (int(start[0] + length * np.sin(np.radians(angle))),
               int(start[1] + length * np.cos(np.radians(angle))))
        draw_vessel(start, end, image)
        angle += np.random.uniform(-10, 10)
        new_length = length * reducer
        new_depth = depth - 1
        draw_tree(end, angle - max_angle * np.random.uniform(-1, 1), new_length, new_depth, image, reducer)
        draw_tree(end, angle + max_angle * np.random.uniform(-1, 1), new_length, new_depth, image, reducer)

    start_point = (height - 1, width // 2)
    initial_angle = -90
    initial_length = np.max((width, height)) * 0.15
    depth = 7
    reducer = 0.9
    draw_tree(start_point, initial_angle, initial_length, depth, image, reducer)
    rectangle = np.ones((lineWidth, lineWidth))
    from scipy.signal import convolve2d
    image = convolve2d(image, rectangle, mode="same", boundary="fill", fillvalue=0)
    return image


if __name__ == "__main__":
    imagePath = "smlm"
    microscope = VirtualMicroscopy(filePath=imagePath)
    vmManager = VirtualMicroscopeManager(rs232Info=type("RS232", (), {"managerProperties": {"imagePath": "smlm"}})(), name="VirtualScope")
    microscope.illuminator.set_intensity(intensity=1000)

    # Toggle objective to simulate switching and doubling magnification via binning
    vmManager.toggleObjective()
    for i in range(5):
        microscope.positioner.move(
            x=1400 + i * (-200), y=-800 + i * (-10), z=0, is_absolute=True
        )
        frame = microscope.camera.getLast()
        plt.imsave(f"frame_{i}.png", frame)
    cv2.destroyAllWindows()

class Objective:
    def __init__(self, parent):
        self._parent = parent





class Camera:
    def __init__(self, parent, filePath="path_to_image.jpeg"):
        self._parent = parent
        self.filePath = filePath

        if self.filePath == "simplant":
            self.image = createBranchingTree(width=5000, height=5000)
            self.image /= np.max(self.image)
            self.SensorHeight = 300  # self.image.shape[1]
            self.SensorWidth = 400  # self.image.shape[0]
        
        elif self.filePath == "astigmatism":
            self.SensorHeight = 512  # self.image.shape[1]
            self.SensorWidth = 512  # self.image.shape[0]

            self.astimulator = AstigmaticMicroscopeSimulator(W=self.SensorHeight, H=self.SensorWidth, roi_half=256)

        elif self.filePath == "smlm":
            self.SensorHeight = 300  # self.image.shape[1]
            self.SensorWidth = 400  # self.image.shape[0]
            
            tmp = createBranchingTree(width=5000, height=5000)
            tmp_min = np.min(tmp)
            tmp_max = np.max(tmp)
            self.image = (
                1 - ((tmp - tmp_min) / (tmp_max - tmp_min)) > 0
            )  # generating binary image
        else:
            self.image = np.mean(cv2.imread(filePath), axis=2)
            self.image /= np.max(self.image)

        self.lock = threading.Lock()
        self.model = "VirtualCamera"
        self.PixelSize = 1.0
        self.isRGB = False
        self.frameNumber = 0
        # precompute noise so that we will save energy and trees
        self.noiseStack = np.abs(
            np.random.randn(self.SensorHeight, self.SensorWidth, 100) * 2
        )

    def produce_frame(
        self, x_offset=0, y_offset=0, z_offset=0, light_intensity=1.0, defocusPSF=None
    ):
        """Generate a frame based on the current settings."""
        if self.filePath == "smlm": # There is likely a better way of handling this
            return self.produce_smlm_frame(x_offset, y_offset, light_intensity)
        elif self.filePath == "astigmatism":
            return self.produce_astigmatism_frame(z_offset)
        else:
            with self.lock:
                # add moise
                image = self.image.copy()
                # Adjust image based on offsets
                image = np.roll(
                    np.roll(image, int(x_offset), axis=1), int(y_offset), axis=0
                )
                image = nip.extract(image, (self.SensorHeight, self.SensorWidth)) # extract the image to the sensor size

                # do all post-processing on cropped image
                if IS_NIP and defocusPSF is not None and not defocusPSF.shape == ():
                    print("Defocus:" + str(defocusPSF.shape))
                    image = np.array(np.real(nip.convolve(image, defocusPSF)))
                image = np.float32(image) * np.float32(light_intensity)
                image += self.noiseStack[:, :, np.random.randint(0, 100)]
                

                # Adjust illumination
                image = image.astype(np.uint16)
                time.sleep(0.1)
                return np.array(image)

    def produce_astigmatism_frame(self, z_offset=0):
        #!/usr/bin/env python3
        return self.astimulator.render_frame(z=z_offset)

    def produce_smlm_frame(self, x_offset=0, y_offset=0, light_intensity=5000):
        """Generate a SMLM frame based on the current settings."""
        with self.lock:
            # add moise
            image = self.image.copy()
            # Adjust image based on offsets
            image = np.roll(
                np.roll(image, int(x_offset), axis=1), int(y_offset), axis=0
            )
            image = np.array(nip.extract(image, (self.SensorHeight, self.SensorWidth)))

            yc_array, xc_array = binary2locs(image, density=0.05)
            photon_array = np.random.normal(
                light_intensity * 5, light_intensity * 0.05, size=len(xc_array)
            )

            wavelenght = 6  # change to get it from microscope settings
            wavelenght_std = 0.5  # change to get it from microscope settings
            NA = 1.2  # change to get it from microscope settings
            sigma = 0.21 * wavelenght / NA  # change to get it from microscope settings
            sigma_std = (
                0.21 * wavelenght_std / NA
            )  # change to get it from microscope settings
            sigma_array = np.random.normal(sigma, sigma_std, size=len(xc_array))

            ADC_per_photon_conversion = 1.0  # change to get it from microscope settings
            readout_noise = 50  # change to get it from microscope settings
            ADC_offset = 100  # change to get it from microscope settings

            out = FromLoc2Image_MultiThreaded(
                xc_array,
                yc_array,
                photon_array,
                sigma_array,
                self.SensorHeight,
                self.SensorWidth,
                self.PixelSize,
            )
            out = (
                ADC_per_photon_conversion * np.random.poisson(out)
                + readout_noise
                * np.random.normal(size=(self.SensorHeight, self.SensorWidth))
                + ADC_offset
            )
            time.sleep(0.1)
            return np.array(out)

    def getLast(self, returnFrameNumber=False):
        position = self._parent.positioner.get_position()
        defocusPSF = np.squeeze(self._parent.positioner.get_psf())
        intensity = self._parent.illuminator.get_intensity(1)
        self.frameNumber += 1
        if returnFrameNumber:
            return (
                self.produce_frame(
                    x_offset=position["X"],
                    y_offset=position["Y"],
                    z_offset=position["Z"],
                    light_intensity=intensity,
                    defocusPSF=defocusPSF,
                ),
                self.frameNumber,
            )
        else:
            return self.produce_frame(
                x_offset=position["X"],
                y_offset=position["Y"],
                z_offset=position["Z"],
                light_intensity=intensity,
                defocusPSF=defocusPSF,
            )


    def getLastChunk(self):
        mFrame = self.getLast()
        return np.expand_dims(mFrame, axis=0), [self.frameNumber] # we only provide one chunk, so we return a list with one element
    
    def setPropertyValue(self, propertyName, propertyValue):
        pass


@njit(parallel=True)
def FromLoc2Image_MultiThreaded(
    xc_array: np.ndarray, yc_array: np.ndarray, photon_array: np.ndarray, sigma_array: np.ndarray, image_height: int, image_width: int, pixel_size: float
):
    """
    Generate an image from localized emitters using multi-threading.

    Parameters
    ----------
    xc_array : array_like
        Array of x-coordinates of the emitters.
    yc_array : array_like
        Array of y-coordinates of the emitters.
    photon_array : array_like
        Array of photon counts for each emitter.
    sigma_array : array_like
        Array of standard deviations (sigmas) for each emitter.
    image_height : int
        Height of the output image in pixels.
    image_width : int
        Width of the output image in pixels.
    pixel_size : float
        Size of each pixel in the image.

    Returns
    -------
    Image : ndarray
        2D array representing the generated image.

    Notes
    -----
    The function utilizes multi-threading for parallel processing using Numba's
    `njit` decorator with `parallel=True`. Emitters with non-positive photon
    counts or non-positive sigma values are ignored. Only emitters within a
    distance of 4 sigma from the center of the pixel are considered to save
    computation time.

    The calculation involves error functions (`erf`) to determine the contribution
    of each emitter to the pixel intensity.

    Originally from: https://colab.research.google.com/github/HenriquesLab/ZeroCostDL4Mic/blob/master/Colab_notebooks/Deep-STORM_2D_ZeroCostDL4Mic.ipynb
    """
    Image = np.zeros((image_height, image_width))
    for ij in prange(image_height * image_width):
        j = int(ij / image_width)
        i = ij - j * image_width
        for xc, yc, photon, sigma in zip(xc_array, yc_array, photon_array, sigma_array):
            # Don't bother if the emitter has photons <= 0 or if Sigma <= 0
            if (photon > 0) and (sigma > 0):
                S = sigma * math.sqrt(2)
                x = i * pixel_size - xc
                y = j * pixel_size - yc
                # Don't bother if the emitter is further than 4 sigma from the centre of the pixel
                if (x + pixel_size / 2) ** 2 + (
                    y + pixel_size / 2
                ) ** 2 < 16 * sigma**2:
                    ErfX = math.erf((x + pixel_size) / S) - math.erf(x / S)
                    ErfY = math.erf((y + pixel_size) / S) - math.erf(y / S)
                    Image[j][i] += 0.25 * photon * ErfX * ErfY
    return Image


def binary2locs(img: np.ndarray, density: float):
    """
    Selects a subset of locations from a binary image based on a specified density.

    Parameters
    ----------
    img : np.ndarray
        2D binary image array where 1s indicate points of interest.
    density : float
        Proportion of points to randomly select from the points of interest.
        Should be a value between 0 and 1.

    Returns
    -------
    filtered_locs : tuple of np.ndarray
        Tuple containing two arrays. The first array contains the row indices
        and the second array contains the column indices of the selected points.

    Notes
    -----
    The function identifies all locations in the binary image where the value is 1.
    It then randomly selects a subset of these locations based on the specified
    density and returns their coordinates.
    """
    all_locs = np.nonzero(img == 1)
    n_points = int(len(all_locs[0]) * density)
    selected_idx = np.random.choice(len(all_locs[0]), n_points, replace=False)
    filtered_locs = all_locs[0][selected_idx], all_locs[1][selected_idx]
    return filtered_locs


def createBranchingTree(width=5000, height=5000, lineWidth=3):
    np.random.seed(0)  # Set a random seed for reproducibility
    # Define the dimensions of the image
    width, height = 5000, 5000

    # Create a blank white image
    image = np.ones((height, width), dtype=np.uint8) * 255

    # Function to draw a line (blood vessel) on the image
    def draw_vessel(start, end, image):
        rr, cc = line(start[0], start[1], end[0], end[1])
        try:
            image[rr, cc] = 0  # Draw a black line
        except:
            end = 0
            return

    # Recursive function to draw a tree-like structure
    def draw_tree(start, angle, length, depth, image, reducer, max_angle=40):
        if depth == 0:
            return

        # Calculate the end point of the branch
        end = (
            int(start[0] + length * np.sin(np.radians(angle))),
            int(start[1] + length * np.cos(np.radians(angle))),
        )

        # Draw the branch
        draw_vessel(start, end, image)

        # change the angle slightly to add some randomness
        angle += np.random.uniform(-10, 10)

        # Recursively draw the next level of branches
        new_length = length * reducer  # Reduce the length for the next level
        new_depth = depth - 1
        draw_tree(
            end,
            angle - max_angle * np.random.uniform(-1, 1),
            new_length,
            new_depth,
            image,
            reducer,
        )
        draw_tree(
            end,
            angle + max_angle * np.random.uniform(-1, 1),
            new_length,
            new_depth,
            image,
            reducer,
        )

    # Starting point and parameters
    start_point = (height - 1, width // 2)
    initial_angle = -90  # Start by pointing upwards
    initial_length = np.max((width, height)) * 0.15  # Length of the first branch
    depth = 7  # Number of branching levels
    reducer = 0.9
    # Draw the tree structure
    draw_tree(start_point, initial_angle, initial_length, depth, image, reducer)

    # convolve image with rectangle
    rectangle = np.ones((lineWidth, lineWidth))
    image = convolve2d(image, rectangle, mode="same", boundary="fill", fillvalue=0)

    return image


if __name__ == "__main__":

    # Read the image locally
    # mFWD = os.path.dirname(os.path.realpath(__file__)).split("imswitch")[0]
    # imagePath = mFWD + "imswitch/_data/images/histoASHLARStitch.jpg"
    imagePath = "smlm"
    microscope = VirtualMicroscopy(filePath=imagePath)
    microscope.illuminator.set_intensity(intensity=1000)

    for i in range(5):
        microscope.positioner.move(
            x=1400 + i * (-200), y=-800 + i * (-10), z=0, is_absolute=True
        )
        frame = microscope.camera.getLast()
        plt.imsave(f"frame_{i}.png", frame)
    cv2.destroyAllWindows()

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
