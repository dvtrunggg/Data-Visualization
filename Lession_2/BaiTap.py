import numpy as np

###3.1
#1
arr = np.linspace(0, 9, 10, dtype=int)
#print(arr, '\n', arr.shape[0], '\n', type(arr))

#2
arr_even = arr[arr % 2 == 0]
#print(arr_even)
arr_odd = arr[arr % 2 != 0]
#print(arr_odd)

#3

arr_update_1 = arr
print(arr_update_1)
listIndex = [i for i in range(arr_update_1.shape[0]) if arr_update_1[i] % 2 != 0]
arr_update_1 = arr

for i in listIndex:
     arr_update_1[i] = 100

print(arr_update_1)