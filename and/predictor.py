import os
from time import time
import cv2 as cv
from typing import List

from ultralytics import YOLO
from ultralytics.yolo.engine.results import Results

model = YOLO('best.pt')

input_dir = "/home/dantas/and_project/AND/AND/images"
file_list = os.listdir(input_dir)

i = 0
total_d = 0.0

for image in file_list:
    source = os.path.join(input_dir, image)

    start = time()
    results: List[Results] = model.predict(source)  # predict on an image
    duration = time() - start

    r =  results[0]
    for b in r.boxes.xyxy:
        print(b)
    for p in r.boxes.conf:
        print(p)
    for c in r.boxes.cls:
        print(type(c), c)
    print(f'Time to infer {duration * 1000}ms')
    plot = r.plot()
    cv.imshow('Image', plot)
    if cv.waitKey(0) == 27:
        exit()

    if i > 0:
        total_d += duration
    i += 1

avg_dur = total_d / i
print(f'Average time to infer: {avg_dur * 1000}ms')