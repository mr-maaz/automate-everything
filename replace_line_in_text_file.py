# Author: Ardit Sulce, Automate Everything with Python, Udemy
# Course URL: https://www.udemy.com/course/automate-everything-with-python/

with open('merged.csv', 'r') as file:
  content = file.readlines()

content[0] = 'ID,AMOUNT,COST\n'

with open('merged.csv', 'w') as file:
  file.writelines(content)
