# version:1.0.1905.9051
import gxipy as gx
from PIL import Image


import napari

def main():
    # create a device manager
    device_manager = gx.DeviceManager()
    dev_num, dev_info_list = device_manager.update_device_list()
    if dev_num == 0:
        print("Number of enumerated devices is 0")
        return

    # open the first device
    cam = device_manager.open_device_by_index(1)

    viewer = napari.Viewer()

    # exit when the camera is a color camera
    if cam.PixelColorFilter.is_implemented() is True:
        print("This sample does not support color camera.")
        cam.close_device()
        return

    binning = 4
    cam.BinningHorizontal.set(binning)
    cam.BinningVertical.set(binning)

    # set continuous acquisition
    cam.TriggerMode.set(gx.GxSwitchEntry.OFF)

    # set exposure
    cam.ExposureTime.set(10000)

    # set gain
    cam.Gain.set(10.0)

    # start data acquisition
    cam.stream_on()

    # acquire image: num is the image number
    num = 1000
    for i in range(num):
        # get raw image
        raw_image = cam.data_stream[0].get_image()
        if raw_image is None:
            print("Getting image failed.")
            continue

        # create numpy array with data from raw image
        numpy_image = raw_image.get_numpy_array()
        if numpy_image is None:
            continue

        # show acquired image
        #img = Image.fromarray(numpy_image, 'L')
        #img.show()
        #cv2.imshow('image',numpy_image)
        #cv2.waitKey(0)
        viewer.add_image(numpy_image)

        # print height, width, and frame ID of the acquisition image
        print("Frame ID: %d   Height: %d   Width: %d"
              % (raw_image.get_frame_id(), raw_image.get_height(), raw_image.get_width()))

    # stop data acquisition
    cam.stream_off()

    # close device
    cam.close_device()

if __name__ == "__main__":
    main()
