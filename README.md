# Raspberry Pi Camera Backup Script

## Usage

1. Connect the camera to the Raspberry Pi.
2. Connect a USB drive to the Raspberry Pi.
3. Activate legacy camera, using `sudo raspi-config` 
3. Run the script using `python3 autocam.py`.
4. The script will capture an image from the camera every 30 minutes and save it to the USB drive.
5. If the USB drive is not found, the images will be saved to the desktop folder `~/Desktop/images`.
6. You may need to change the camera index in the script, e.g. `cap = cv2.VideoCapture(0)` if the camera is not detected.
7. Press Ctrl+C to stop the script.

## Requirements

- Fully Set up Raspberry Pi 
- USB drive
- OpenCV

## Camera Test
 
- To test, if the camera is working, type: `python3 cam_test.py`

## Notes

- If the folder `images` doesn't exist on the USB drive, the script will create it automatically.
- If you encounter a permission error when running the script, make sure you have the necessary permissions to access the camera and USB drive.
