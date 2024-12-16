#Reverse a integer number-----------------
num=76542
rev=0
print("given number ",num)
while num>0:
    rem=num%10
    rev=(rev*10)+rem
    num=num // 10
print("reverse number", rev)
