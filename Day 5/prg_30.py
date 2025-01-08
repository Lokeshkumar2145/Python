'''Write a Python program to check whether a file exists'''
import os
filepath="test.py"
if os.path.exists(filepath):
    print(f"The file '{filepath}' exists.")
else:
    print(f"The file '{filepath}' does not exist.")
