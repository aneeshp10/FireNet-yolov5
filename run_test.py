import torch
import os
from matplotlib import pyplot as plt
import numpy as np
from PIL import Image

model = torch.hub.load('ultralytics/yolov5', 'custom', path='yolov5/runs/train/exp7/weights/last.pt', force_reload=True)
img = os.path.join('data', 'images', '1438.jpg')
result = model('fire_ext10.jpg')

img_dim = Image.open('fire_ext10.jpg')
width = img_dim.width
height = img_dim.height
dict_output = {"width": width, "height": height,
               "detection":
                   {
                       
                    }
               }


result.print()
result.show()

