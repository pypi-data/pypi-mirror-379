from setuptools import setup, find_packages


# Version will be read from your package's __init__.py
# Make sure __version__ is defined in imswitch/__init__.py
def get_version():
    version_file = 'imswitch/__init__.py'
    with open(version_file, 'r') as file:
        for line in file:
            if line.startswith('__version__'):
                # Strip the line to remove whitespaces and newline characters,
                # then split it on '=' and strip again to remove any remaining whitespaces.
                # Finally, strip the quotes from the version string.
                return line.strip().split('=')[1].strip().strip('\'"')
    raise RuntimeError('Unable to find version string.')


# NOTE: This setup.py is maintained for backward compatibility.
# The primary configuration is now in pyproject.toml for UV support.
# When using UV, this file is not needed, but it's kept for pip compatibility.


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="ImSwitchUC2",
    version=get_version(),
    author="Benedict Diederich, Xavier Casas Moreno, et al.",
    author_email="benedictdied@gmail.com",
    description="Microscopy control",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/openuc2/ImSwitch",
    project_urls={
        "Bug Tracker": "https://github.com/openuc2/ImSwitch/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    include_package_data=True,
    python_requires=">=3.10",
    install_requires=[
        "pydantic==2.11.4",
        "coloredlogs >= 15",
        "colour-science >= 0.3",
        "dataclasses-json >= 0.5",
        "h5py >= 2.10",
        "pyvisa-py==0.4.1",
        "lantzdev >= 0.5.2",
        "luddite >= 1",
        "nidaqmx >= 0.5.7",
        "numpy==2.0.2",
        "packaging >= 19",
        "psutil >= 5.4.8",
        "pyserial >= 3.4",
        "requests >= 2.25",
        "scikit-image==0.25.2",
        "Send2Trash >= 1.8",
        "tifffile >= 2020.11.26",
        "dask[complete] >= 2024.8.0",
        "fastAPI >= 0.86.0",
        "uvicorn[standard] >= 0.19.0",
        "matplotlib == 3.9.2",
        "opencv-python",
        "dataclasses-json >= 0.5",
        "aiortc >= 1.9.0",
        "UC2-REST",
        "tk >= 0.1.0",
        "jupyter",
        "python-multipart >= 0.0.5",
        "piexif >= 1.1.3",
        "NanoImagingPack==2.1.4",
        "imswitchclient>=0.1.2",
        "psygnal",
        "python-socketio[asyncio]==5.11.4",
        "jupyterlab==4.2.5",
        "python-dateutil >= 2.8.1",
        "zarr>=3",
        "numcodecs>=0.13.1",
        "aiohttp>=3.9.4",
        "numba>=0.61.2"
        ],

     extras_require={ # we assume that this is installed in a conda environment or via apt-get
        'PyQt5': [
            "qtpy >= 1.9",
            "PyQt5 >= 5.15.2",
            "QDarkStyle >= 3",
            "QScintilla >= 2.12",
            "PyQtWebEngine >= 5.15.2",
            "pyqtgraph >= 0.12.1",
            "napari[pyqt5] == 0.6.4",
            "lantzdev[qt] >= 0.5.2",
            "qtpy >= 1.9"
        ],
        'Lepmon': [
            "RPi.GPIO",
            "luma.oled",
            "smbus2",
            "smbus"
        ],
        'Ashlar': [
            "ashlarUC2"
        ],
        'arkitekt':
            [
            "arkitekt==0.7.8",
            "arkitekt_next>=0.8.6"
        ],
        'imjoy':[
            "imjoy-rpc==0.5.59",
            "imjoy_rpc",
            "imjoy",
        ],
        # Test dependencies for API testing
        'testing': [
            "pytest>=6.0",
            "pytest-asyncio",
            "requests>=2.25",
            "httpx>=0.24.0",  # Alternative HTTP client for async testing
        ],
        },

    entry_points={
        "console_scripts": [
            "imswitch = imswitch.__main__:main",
        ],
        'imswitch.implugins.detectors': [],
        'imswitch.implugins.lasers': [],
        'imswitch.implugins.positioner': [],
        "jupyter.kernel_provisioners": [ # has to point to jupyter_connection.py -> ExistingProvisioner
            "imswitch-provisioner = imswitch.imcontrol.model.jupyter_connection:ExistingProvisioner",
        ]
    },
)

# For NIP install it using:
# python -m pip install https://gitlab.com/bionanoimaging/nanoimagingpack/-/archive/master/nanoimagingpack-master.zip

# Note: Automatic version bumping is now enabled via GitHub Actions
