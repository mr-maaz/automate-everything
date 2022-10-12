# Author: Ardit Sulce, Automate Everything with Python, Udemy
# Course URL: https://www.udemy.com/course/automate-everything-with-python/

from forex_python.converter import CurrencyRates
import datetime

c = CurrencyRates()

dt = datetime.datetime(2020, 3, 27, 11, 21, 13, 114505)

print(c.get_rate('USD', 'INR', dt))
