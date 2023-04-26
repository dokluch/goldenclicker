import cv2
from mss import mss
from mss import tools as msstools
import time
import pyautogui
import numpy as np
from classes import Counter
import asyncio
from yolo_ops import build_model, detect, format_yolov5, load_classes, wrap_detection
from datetime import datetime
from pathlib import Path

class_list = load_classes()
colors = [(255, 255, 0), (0, 255, 0), (0, 255, 255), (255, 0, 0)]
is_cuda = False
net = build_model(is_cuda)
default_pause = 5

def format_datetime_for_filename():
    now = datetime.now()
    return now.strftime("%Y-%m-%d_%H-%M-%S")


async def click_coorditates(coordinates):
    pyautogui.moveTo(coordinates[0], coordinates[1])
    # Click the left mouse button
    pyautogui.click(button='left')
    time.sleep(0.005)

# Define endpoint to accept file uploads
async def predict(png_data, goldenclicks, wrathclicks, handclicks, deerclicks, spookyclicks, bunnyclicks):
    """
    Get YOLO predictions and click if there are boxes with suitable type
    """

    frame = cv2.imdecode(np.frombuffer(png_data, dtype=np.uint8), cv2.IMREAD_COLOR)
    inputImage = format_yolov5(frame)
    outs = detect(inputImage, net)

    class_ids, confidences, boxes = wrap_detection(inputImage, outs[0])


    if boxes:
        for class_id, box in zip(class_ids, boxes):
            coordinates = (box[0] + box[2] / 2, box[1] + box[3] / 2)

            if class_id == 1:
                #Golden Cookie
                goldenclicks.increment()
                await click_coorditates(coordinates)
                print(goldenclicks)
            
            if class_id == 2:
                #Wrath Cookie
                wrathclicks.increment()
                await click_coorditates(coordinates)
                print(wrathclicks)

            if class_id == 3:
                # Hand of Fate Spell
                handclicks.increment()
                await click_coorditates(coordinates)
                print(handclicks)

            if class_id == 5:
                # Deers clicked
                deerclicks.increment()
                await click_coorditates(coordinates)
                print(deerclicks)


            if class_id == 6:
                # Spooky clicked
                spookyclicks.increment()
                await click_coorditates(coordinates)
                print(spookyclicks)

            if class_id == 7:
                # Bunnies clicked
                bunnyclicks.increment()
                await click_coorditates(coordinates)
                print(bunnyclicks)

            #     cv2.imwrite(str(output_folder.joinpath(format_datetime_for_filename()).with_suffix(".png")), frame)


    # if len(boxes) > 5:
    #     # Account for lots of cookies, click everything
    #     return 0.01
    return default_pause
            

async def makescreenshot():
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
    goldenclicks = Counter(1, "Golden cookies")
    wrathclicks = Counter(2, "Wrath cookies")
    handclicks = Counter(4, "Hands of Fate")
    deerclicks = Counter(5, "Deers")
    spookyclicks = Counter(6, "Spooky")
    bunnyclicks = Counter(7, "Bunnies")

    async def main():
        while True:
            screenshot = await makescreenshot()
            pause = await predict(screenshot, 
                                  goldenclicks, 
                                  wrathclicks, 
                                  handclicks, 
                                  deerclicks, 
                                  spookyclicks,
                                  bunnyclicks)
            
            await asyncio.sleep(pause)

    asyncio.run(main())