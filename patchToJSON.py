import torch
import os
import json
from matplotlib import pyplot as plt
import numpy as np
from PIL import Image

class_dict = {0: "Alarm Activator", 1: "Fire Blanket", 2: "Fire Exit", 3: "Fire Extinguisher",
         4: "Fire Suppression Signage", 5: "Flashing Light Orbs", 6: "Sounders", 7: "White Domes"} # class names

model = torch.hub.load('ultralytics/yolov5', 'custom', path='yolov5/runs/train/exp/weights/last.pt', force_reload=True)
img = os.path.join('data', 'images', '1438.jpg')
#result = model('tesfire_ext7.jpg')


os.system("python yolov5/detect.py --weights yolov5/runs/train/exp/weights/last.pt "
          "--source test/ --save-txt --save-conf")

dir_path = "yolov5/runs/detect"

# find the last experiment in the detect folder
last_exp = ""
for filename in os.listdir(dir_path):
    print(filename)
    last_exp = os.path.join(dir_path, filename)


#print(last_exp)
labels_dir = os.path.join(last_exp, "labels")
for filename in os.listdir(labels_dir):
    print(filename)
    curr = os.path.join(labels_dir, filename)
    print(curr)
    if os.path.isfile(curr):
        data = {"width": 640, "height": 640,
                "detections": []
                }
        with open(curr) as f:
            lines = f.readlines()
            for line in lines:
                str_arr = line.split()
                print("hiiii" + line)
                tmp_detection = {"class": class_dict[int(str_arr[0])], "x": str_arr[1], "y": str_arr[2],
                                 "width": str_arr[3], "height": str_arr[4], "score": str_arr[5]}
                data["detections"].append(tmp_detection)

    json_string = json.dumps(data)
    print(json_string)
    with open(curr[:-4]+'.json', 'w') as outfile:
        outfile.write(json_string)


#result.print()
#result.show()
