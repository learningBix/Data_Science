import numpy as np
import sys
list = list(range(1,101))
print(list)

array = np.arange(1,101)
print(array)

print(f'size of each element of list is {sys.getsizeof(list)}')
print(f'total size of  list is {sys.getsizeof(list)*len(list)}')

print(f'size of each element of array is {array.itemsize}')
print(f'total size of  array is {array.itemsize*array.size}')

