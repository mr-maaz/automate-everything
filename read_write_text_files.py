# Author: Ardit Sulce, Automate Everything with Python, Udemy
# Course URL: https://www.udemy.com/course/automate-everything-with-python/

content = """First text


Second text"""

with open('file1.txt', 'w') as file:
  file.write(content)
