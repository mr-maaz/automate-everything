# Author: Ardit Sulce, Automate Everything with Python, Udemy
# Course URL: https://www.udemy.com/course/automate-everything-with-python/

import qrcode

img = qrcode.make('https://google.com')
img.save('qr1.png')
