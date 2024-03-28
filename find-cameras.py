import pyudev

def find_cameras():
    context = pyudev.Context()
    cameras = []
    
    for device in context.list_devices(subsystem='video4linux'):
        cameras.append(device.device_node)
    
    return cameras

if __name__ == "__main__":
    cameras = find_cameras()
    if len(cameras) == 0:
        print("No cameras found.")
    elif len(cameras) == 1:
        print("One camera found at port:", cameras[0])
    else:
        print("Multiple cameras found at ports:", cameras)