
'''23. Write a Python program to find the available built-in modules'''

import sys

builtin_modules = sys.builtin_module_names
print("Available built-in modules:")
for module in builtin_modules:
    print(module)