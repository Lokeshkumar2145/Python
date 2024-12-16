'''1. Write a Python program which accepts the user's first and last name and print them in
reverse order with a space between them.
'''

f_name=input("enter your first name : ")
l_name=input("enter your last name : ")
print(f_name[::-1] + " "+l_name[::-1])