#!/usr/bin/env python3

import os
import time
import cv2
import datetime 


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
def FindCameras():
    # checks the first 20 indexes.
    index = 0
    arr = []
    i = 20
    while i > 0:
        cap = cv2.VideoCapture(index)
        if cap.read()[0]:
            arr.append(index)
            cap.release()
        index += 1
        i -= 1
    return arr



def main():
    # Define root save directory
    root_dir = "Recorded-Images/Test"
    if not os.path.exists(root_dir):
        os.makedirs(root_dir)

    # Finding cameras
    print("Searching for cameras...")
    cams = FindCameras()
    noCams = len(cams) 
    print(noCams, " cameras found.")

    #Autoassign the cameras
    for index in cams: 

        # Make directory
        save_dir = os.path.join(root_dir, f"Camera{index}") 
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
        
        # Take picture: 
        capture_picture(index, save_dir)

        # Wait 2 seconds
        print("Waiting for 2 seconds between cameras...")
        time.sleep(1)

    # Wait for 2 minutes
    print("Waiting for 2 minutes before capturing pictures...")
    
    # Put wait time here: ###########################################################
    wait_time = 60
    time_adjusted = wait_time - noCams*1
    
    if time_adjusted < 0:
        time_adjusted = 0
    
    
    time.sleep(time_adjusted)


if __name__ == "__main__":
    
    while True:
        main()