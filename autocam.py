import cv2
import time
import shutil
import os

# set up the camera
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

# set up the file name and directory for the images
directory = "/home/pi/Desktop/images/"
file_prefix = "image_"

# set up the USB drive backup
usb_directory = "/media/pi/USB/images/"
if not os.path.exists(usb_directory):
    os.makedirs(usb_directory)

while True:
    # get the current time
    current_time = time.strftime("%Y-%m-%d-%H-%M-%S", time.gmtime())

    # capture a frame from the camera
    ret, frame = cap.read()

    # save the frame as an image file
    file_name = directory + file_prefix + current_time + ".jpg"
    cv2.imwrite(file_name, frame)

    # backup the file to USB
    try:
        usb_file_name = usb_directory + file_prefix + current_time + ".jpg"
        shutil.copy(file_name, usb_file_name)
    except:
        pass

    # wait for 30 minutes before taking the next picture
    time.sleep(1800)
