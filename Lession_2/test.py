#!/usr/bin/env python
# coding: utf-8

# ## Chapter 3 - Exercise 1a: Thực hiện các yêu cầu sau, và đối chiếu với kết quả cho trước

# In[1]:


import numpy as np


# In[33]:


# Câu 1: Tạo numpy array có giá trị từ 0-9 và lưu vào biến arr
arr = np.arange(0, 10, dtype = int)

# Hiển thị các phần tử có trong arr
print(arr)

# Xem kiểu dữ liệu (type) của arr
print('type of array: ', type(arr))

# Xem kích thước (shape) của arr
print('size of array: ', arr.shape[0])


# <details>
#   <summary>Nhấn vào đây để xem kết quả!</summary>
#   <pre>[0 1 2 3 4 5 6 7 8 9]
# &lt;class 'numpy.ndarray'&gt;
# (10,)
# </pre>
#   
# </details>

# In[34]:


# Câu 2: Từ array arr ở câu 1 => tạo arr_odd và arr_even 
arr_even = arr[arr % 2 == 0]
arr_odd = arr[arr % 2 != 0]

# Hiển thị các phần tử có trong arr_odd và arr_even
print('arr_even = ', arr_even)
print('arr_odd = ', arr_odd)


# <details>
#   <summary>Nhấn vào đây để xem kết quả!</summary>
#   <pre>Odd array:
# [1 3 5 7 9]
# Event array:
# [0 2 4 6 8]
# </pre>
#   
# </details>

# In[35]:


# Câu 3: Từ array arr ở câu 1=> tạo arr_update_1 với các phần tử chẵn giữ nguyên, các phần tử lẻ thay bằng 100
arr_update_1 = arr
print(arr_update_1)

#mảng vị trí chứa phần tử lẻ
oddIndexArr = [i for i in range(arr_update_1.shape[0] - 1) if arr_update_1[i] % 2 != 0]
for i in oddIndexArr:
    arr_update_1[i] = 100   

# Hiển thị các phần tử có trong arr_update_1
print('arr_update_1', arr_update_1)


# <details>
#   <summary>Nhấn vào đây để xem kết quả!</summary>
#   <pre>[  0 100   2 100   4 100   6 100   8 100]
# </pre>
#   
# </details>
