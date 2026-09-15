#min() vs max() vs sum()
import math
a=[10,66,45,89,32,2,1,56]
print(max(a))#89 give the maximu value in list
print(min(a))# 1 give the minimum value in the list
print(sum(a))# 301give the sum of the element in the list
# min and max directly index nhi dete if u typecast then they give index of max ayur min value

print(a.index(max(a)))# 89 is the maximum value at index 3
print(a.index(min(a)))# 1 is the minimum value at index 6

#if datatype are mixed in one list then give typeerror
b=[10,20 ,'30',40,50]
print(max(b))