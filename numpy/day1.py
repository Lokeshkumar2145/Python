# how to create arrays using numpy
"""
--> numpy is a library functions
-->NumPy is a Python library used for working with arrays
-->
"""


#merits
"""
-->faster and contiguous memory
-->convience
-->Memory efficient
-->Multi-dimensional Arrays
-->rich in mathematical functions and statistical functions

"""

import numpy as np

#creating 1d Array
n1=np.array([1,2,3,4])
print(n1)

#creating 2d Array
n2=np.array([[1,2,3,4],[5,6,7,8]])
print(n2)

#creating 3d Array
n3=np.array([[[1,2,3,4],[5,6,7,8]],[[4,3,2,1],[9,8,7,6]]])
print(n3)
# to check no of dimensions
print(n3.ndim)

#creating a zero filled  2d array with speccifing datatype
n4=np.zeros([4,5],dtype='int32')
print(n4)

#creating a ones filled  2d array with speccifing datatype
n4=np.ones([2,3,3],dtype='int32')
print(n4)

# creating a empty array- contains random junk values
n5=np.empty([1,3])
print(n5)

# creating an array with arange specified
n6=np.arange(0,10)
print(n6)

# creating an array with arange specified , with start , stop , step
n7=np.arange(-5,30,5)
print(n7)

# creating an array with linear spaced entries
n7=np.linspace(0,30,num=5)
print(n7)

# creating an array with full
n8=np.full([3,2],100)
print(n8)

# creating an array with fill
n8=np.fill([3,2],100)
print(n8)   