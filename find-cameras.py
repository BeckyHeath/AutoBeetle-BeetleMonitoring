import cv2

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

indexes = FindCameras()

print(indexes)