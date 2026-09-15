e=[1,2,3,4]
a,b,c,d=e
print(a)
print(b)
print(c)
print(d)#his is the way u unpack the vlue of list into a variable
#but if jitni value h unte variable hone cheya for unpack the list value

a,*y=e
print(a)
print(*y) #using astrik to unpack all value at once

a = [10, 20, 30, 40, 50]

x, *y, z = a

print(x)
print(y)
print(z)