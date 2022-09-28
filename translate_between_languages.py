# Author: Ardit Sulce, Automate Everything with Python, Udemy
# Course URL: https://www.udemy.com/course/automate-everything-with-python/

from googletrans import Translator

translator = Translator()

translation = translator.translate('Oa mai oe?', dest='en').text

print(translation)
