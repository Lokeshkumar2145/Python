'''print these when a dice  rolled to a random number --> . : :. :: ::. ::: '''
import random

def fun():
    dice=random.randint(0,6)
    if dice==1:
        return "|.|"
    if dice==2:
        return "|:|" or "|..|"
    if dice==3:
        return "|:.|" or "|.:|"
    if dice==4:
        return "|::|"
    if dice==5:
        return "|::.|" or "|.::|"
    else:
        return "|:::|"

print(fun())