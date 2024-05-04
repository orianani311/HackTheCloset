import requests
import shutil
import pandas as pd
import os
from PIL import Image
import json

mypath = "./website/data/"
csv_path = "./website/images_men.csv"
df = pd.read_csv(csv_path)
color_list = []
for ind in df.index:
    #print(df.loc[ind])
    row = df.loc[ind].dropna()
    for url in row:
        print(url)
        image_path = mypath + url.replace("/", "_").replace("?", "-").replace(".", "-").replace(":", "-")
        img = Image.open(image_path)
        size = img.size
        middle_x = size[0] // 2
        middle_y = size[1] // 2
        
        # Define the size of the box (e.g., 100x100)
        box_width = 30
        box_height = 30
        
        # Calculate the coordinates of the corners of the box
        top_left = (middle_x - box_width // 2, middle_y - box_height // 2)
        top_right = (middle_x + box_width // 2, middle_y - box_height // 2)
        bottom_left = (middle_x - box_width // 2, middle_y + box_height // 2)
        bottom_right = (middle_x + box_width // 2, middle_y + box_height // 2)
        
        corner_pixels = [
            img.getpixel((middle_x, middle_y)),
            img.getpixel(top_left),
            img.getpixel(top_right),
            img.getpixel(bottom_left),
            img.getpixel(bottom_right)
        ]

        color_list.append(corner_pixels)
json_object = json.dumps(color_list, indent=4)
with open("color.json", "w") as outfile:
    outfile.write(json_object)
