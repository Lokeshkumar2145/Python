'''Write a Python program to count the number occurrence of a specific character in a string.'''

str="lokesh kumar"
ch="k"
sum=0
for i in str:
    if i==ch:
        sum+=1
print(f"the number of {i} occurences is -->",sum)
