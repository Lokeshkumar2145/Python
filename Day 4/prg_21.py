'''2. Write a Python program which accepts a sequence of comma-separated numbers from user
and generate a list and a tuple with those numbers.
Sample data : 3, 5, 7, 23
Output :
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')
'''

str=input("enter the str with comma seperated numbers or words - ex ->'123,word' : ")
strlist=str.split(",")
strtuple=tuple(str.split(","))
print(type(str))
print(type(strlist))
print(strlist)
print(type(strtuple))
print(strtuple)