'''Write a Python program to get numbers divisible by fifteen from a list using an anonymous
function.'''
ls1=[]
def fun(x,y):
    ls=x
    num=y
    for i in ls:
        if i%num==0:
            global ls1
            ls1.append(i)
    return ls1

print(fun([15,23,30,45,96,32],15))
