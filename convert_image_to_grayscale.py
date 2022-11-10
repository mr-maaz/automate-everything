# Author: Ardit Sulce, Automate Everything with Python, Udemy
# Course URL: https://www.udemy.com/course/automate-everything-with-python/

import cv2

color = cv2.imread('galaxy.jpeg', 0)
cv2.imwrite('galaxy-gray.jpeg', color)
