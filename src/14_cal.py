"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime

today = datetime.now()
month = today.month
year = today.year

input("Enter the year and month in the following format: 2020 01:")

args = sys.argv

tc = calendar.TextCalendar()

if len(args) == 1:
	print(tc.prmonth(year, month))

elif len(args) == 2:
	month = int(args[1])
	print(tc.prmonth(year, month))

elif len(args) == 3:
	month = int(args[1])
	year = int(args[2])
	print(tc.prmonth(year, month))

else:
	print("Input should be in this format: `14_cal.py month [year]`")

# input_list = []

# user_input = input("Enter the month and year as digits separated by a comma(ex: 02, 2012): ").replace(" ", "").split(",")

# def new_calendar(month=default_month, year=default_year):
# 	if len(user_input) == 0:
# 		print(calendar.TextCalendar().formatmonth(default_year, default_month))
	# elif len(user_input) == 1:
	# 	print(calendar.TextCalendar().formatmonth(default_year, default_month))