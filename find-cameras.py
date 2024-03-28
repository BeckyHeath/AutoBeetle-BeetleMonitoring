import pyudev

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

if __name__ == "__main__":
    cameras = find_cameras()
    if not cameras:
        print("No cameras found.")
    elif len(cameras) == 1:
        identifier, port = next(iter(cameras.items()))
        print(f"One camera found with identifier {identifier} at port: {port}")
    else:
        print("Multiple cameras found:")
        for identifier, port in cameras.items():
            print(f"- Identifier: {identifier}, Port: {port}")
