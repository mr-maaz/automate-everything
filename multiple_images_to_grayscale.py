# Author: Ardit Sulce, Automate Everything with Python, Udemy
# Course URL: https://www.udemy.com/course/automate-everything-with-python/

import os
import cv2

images = os.listdir('images')
for image in images:
  print(image)
  gray = cv2.imread(f'images/{image}', 0)
  print(gray)
  cv2.imwrite(f'grayimages/gray-{image}', gray)
