import cv2
from mss import mss
from mss import tools as msstools
import time
import pyautogui
import numpy as np
from classes import Counter

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
def predict(png_data, goldenclicks):
    """
    Get YOLO predictions and click if there are boxes with suitable type
    """
    frame = cv2.imdecode(np.frombuffer(png_data, dtype=np.uint8), cv2.IMREAD_COLOR)
    inputImage = format_yolov5(frame)
    outs = detect(inputImage, net)

    class_ids, confidences, boxes = wrap_detection(inputImage, outs[0])

    if boxes:
        for class_id, box in zip(class_ids, boxes):
            if class_id != 1:
                continue

            goldenclicks.increment()
            click_coorditates(box[0], box[1])
            print(f"Golden cookies clicked: {goldenclicks.counter}")
            

def makescreenshot():
    """
    Makes a screenshot with MSS directly to the memory
    """
    with mss() as sct:
        monitor = sct.monitors[1]
        sct_img = sct.grab(monitor)

        # Screenshot is not saved locally
        png = msstools.to_png(sct_img.rgb, sct_img.size)
        return png

if __name__ == "__main__":
    goldenclicks = Counter()
    # time.sleep(3)
    while True:
        screenshot = makescreenshot()
        predict(screenshot, goldenclicks)
        time.sleep(10)