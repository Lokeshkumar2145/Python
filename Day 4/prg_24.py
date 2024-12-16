"""Write a Python program to print the calendar of a given month and year.
Note : Use 'calendar' module."""

import calendar

year=input()

cal = calendar.month(year, month)
print(cal)