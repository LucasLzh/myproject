from django.test import TestCase
import datetime
year = str(datetime.datetime.now().year)
month = str(datetime.datetime.now().month)
if len(month) == 1:
    month = "0" + month
print(year, month)
# Create your tests here.
