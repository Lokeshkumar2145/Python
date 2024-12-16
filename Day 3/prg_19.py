'''33. Write a Python program to convert a month name to a number of days.
Expected Output:

List of months: January, February, March, April, May, June, July, August
, September, October, November, December
Input the name of Month: February
No. of days: 28/29 days'''

dict1={
    'January':31,
    'February':28/29,
    'March':31,
    'April':30,
    'May':31,
    'June':30,
    'July':31,
    'August':31,
    'September':30,
    'October':31,
    'November':30,
    'December':31
}
str=input("enter the month name")
for i in dict1:
    if i==str.capitalize():
        print(dict1.values)
