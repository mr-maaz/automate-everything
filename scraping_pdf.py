# Author: Ardit Sulce, Automate Everything with Python, Udemy
# Course URL: https://www.udemy.com/course/automate-everything-with-python/

import fitz

with fitz.open("students.pdf") as pdf:
  text = ''
  for page in pdf:
    text = text + page.get_text()
    print(text)
