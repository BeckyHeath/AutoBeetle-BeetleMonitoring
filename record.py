#!/usr/bin/env python3

import os
import time
import cv2
import datetime 
import pyudev

# Updated Tues 2pm UK 
# TEST VERSION ONLY


# Function to capture picture from camera
def capture_picture(camera_index, save_dir):
    # Open camera
    camera = cv2.VideoCapture(camera_index)
    if not camera.isOpened():
        print(f"Error: Unable to open camera {camera_index}")
        return
    
    # Capture picture

    # ret is a boolean value true/ false on whether an image was captures
    # frame is the array of values 
    ret, frame = camera.read()


    if ret:
        # Save picture
        timestamp = datetime.datetime.now()
        filename = os.path.join(save_dir, f"camera_{camera_index}_{timestamp}.jpg")
        cv2.imwrite(filename, frame)
        print(f"Picture captured from camera {camera_index} and saved as {filename}")
    else:
        print(f"Error: Unable to capture picture from camera {camera_index}")
    
    # Release camera
    camera.release()

# Function to find cameras - check it works seperately
def find_cameras():
    context = pyudev.Context()
    cameras = {}

    for device in context.list_devices(subsystem='video4linux'):

        # Check if the device is a video capture device
        if 'ID_V4L_CAPABILITIES' in device and 'video_capture' in device['ID_V4L_CAPABILITIES']:
            
            # Extract unique identifier for the camera
            identifier = device.get('ID_SERIAL_SHORT') or device.get('ID_SERIAL')
            
            if identifier:
                # Add camera to the dictionary with its identifier
                cameras[identifier] = device.device_node
    
    return cameras



def main():
    # Define root save directory
    root_dir = "Recorded-Images/Test"
    if not os.path.exists(root_dir):
        os.makedirs(root_dir)

    # Finding cameras
    print("Searching for cameras...")
    cams = find_cameras()
    noCams = len(cams) 
    print(noCams, " cameras found.")

    #Autoassign the cameras
    for identifier, port in cams.items(): 
        index = ''.join(c for c in port if c.isdigit())

        # Make directory
        save_dir = os.path.join(root_dir, f"Camera{index}") 
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
        
        # Take picture: 
        capture_picture(index, save_dir)

        # Wait 2 seconds
        print("Waiting for 2 seconds between cameras...")
        time.sleep(2)

    # Wait for 2 minutes
    print("Waiting for 2 minutes before capturing pictures...")
    time.sleep(120)


if __name__ == "__main__":
    
    while True:
        main()