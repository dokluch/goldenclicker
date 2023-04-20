import cv2
from mss import mss
from mss import tools as msstools
import time
import pyautogui
import numpy as np

from yolo_ops import build_model, detect, format_yolov5, load_classes, wrap_detection

class_list = load_classes()
colors = [(255, 255, 0), (0, 255, 0), (0, 255, 255), (255, 0, 0)]
is_cuda = False
net = build_model(is_cuda)

def click_coorditates(x, y):
    pyautogui.moveTo(x, y)
    # Click the left mouse button
    pyautogui.click(button='left')
    time.sleep(0.01)

# Define endpoint to accept file uploads
def predict(png_data):
    """
    Get YOLO predictions and click if there are boxes with suitable type
    """
    frame = cv2.imdecode(np.frombuffer(png_data, dtype=np.uint8), cv2.IMREAD_COLOR)
    inputImage = format_yolov5(frame)
    outs = detect(inputImage, net)

    class_ids, confidences, boxes = wrap_detection(inputImage, outs[0])
    print(confidences)

    if boxes:
        for box in boxes:
            click_coorditates(box[0], box[1])
            

def makescreenshot():
    """
    Makes a screenshot with MSS directly to the memory
    """
    with mss() as sct:
        monitor = sct.monitors[1]
        sct_img = sct.grab(monitor)

        # Screenshot is not saved locally
        png = msstools.to_png(sct_img.rgb, sct_img.size)
        predict(png)

if __name__ == "__main__":
    # time.sleep(3)
    while True:
        makescreenshot()
        time.sleep(10)