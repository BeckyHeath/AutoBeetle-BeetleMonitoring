import os
import time
import cv2

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
        timestamp = int(time.time())
        filename = os.path.join(save_dir, f"camera_{camera_index}_{timestamp}.jpg")
        cv2.imwrite(filename, frame)
        print(f"Picture captured from camera {camera_index} and saved as {filename}")
    else:
        print(f"Error: Unable to capture picture from camera {camera_index}")
    
    # Release camera
    camera.release()

def main():
    # Define root save directory
    root_dir = "Recorded-Images/Test"
    if not os.path.exists(root_dir):
        os.makedirs(root_dir)

    # Wait for 30 minutes
    print("Waiting for 30 minutes before capturing pictures...")
    time.sleep(10)

    # Set output directory for Camera 1
    save_dir01 = root_dir + "/Camera01"
    if not os.path.exists(save_dir01):
        os.makedirs(save_dir01)

    # Capture picture from camera 1
    capture_picture(0, save_dir01)

    # Wait for 10 seconds
    print("Waiting for 10 seconds...")
    time.sleep(2)

    # Set output directory for camera 2
    save_dir02 = root_dir + "/Camera02"
    if not os.path.exists(save_dir02):
        os.makedirs(save_dir02)

    # Capture picture from camera 2
    capture_picture(0, save_dir02)

if __name__ == "__main__":
    main()