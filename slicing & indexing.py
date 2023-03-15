import numpy as np

one_d_array = np.random.randint(1,20,40)
print(one_d_array)

sliced_data =  one_d_array[10:20]
print(f'sliced data is{sliced_data}')


print(one_d_array[-3])


two_d_array = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(two_d_array)

# arry[start_row:end_row,start_column:end_column]
print(two_d_array[2:,2:])