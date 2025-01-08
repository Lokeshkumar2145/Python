'''9. Write a Python program to concatenate all elements in a list into a string and return it.
'''

def fun(x):
    ls=x
    sum=0
    for i in ls:
        sum = sum + i
    return sum



str=fun([4,3,6,1])
print(str)