'''
import os

training_labels = os.listdir("/Users/multicampus/Desktop/SSAFY/PJT2/SUB_PJT2/음식이미지샘플/")
f = open("labels.txt", "w")
for training_label in training_labels:
    f.write(training_label + "\n")
f.close()
'''

# xml
from PIL import Image
import os

"""
mode_to_bpp = {"1": 1, "L": 8, "P": 8, "RGB": 24, "RGBA": 32, "CMYK": 32, "YCbCr": 24, "LAB": 24, "HSV": 24, "I": 32, "F": 32}
bpp = mode_to_bpp[im.mode]
if bpp == 24:
"""

absolute_path = "/Users/multicampus/Desktop/SSAFY/PJT2/YOLO2/darkflow/train"
for file in os.listdir(absolute_path + "/images"):
    if file.endswith("jpg"):
        im = Image.open(absolute_path + "/images/" + file)
        if im.mode == "RGB":
            _, _ , w, h  = im.getbbox()
            
            objName, _ = file.split(' ')

            s = "<annotation> <folder> images </folder> <filename>"
            s += file
            s += "</filename> <size> <width>"
            s += str(w)
            s += "</width> <height>"
            s += str(h)
            s += "</height>	<depth>3</depth></size>	<segmented>0</segmented><object><name>"
            s += objName
            s += "</name><pose>Left</pose><truncated>1</truncated><difficult>0</difficult><bndbox><xmin>0</xmin><ymin>0</ymin><xmax>"
            s += str(w)
            s += "</xmax><ymax>"
            s += str(h)
            s += "</ymax>	</bndbox></object>	</annotation>"

            f = open(absolute_path + "/Annotations/" + file + ".xml", "w")
            f.write(s)
            f.close()