"""
A date in Python is not a data type of its own, but we can import a module named datetime to work with dates as date objects.

The datetime() class requires three parameters to create a date: year, month, day.

The datetime object has a method for formatting date objects into readable strings.

The method is called strftime(), and takes one parameter, format, to specify the format of the returned string:
"""

import datetime

x = datetime.datetime.now()
print(x)
