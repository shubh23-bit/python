# l=["Python", "Java", "C++", "JavaScript", "Go"]
# print(l[0])
# print(l[3])
# print(l[-1])
# print(l[-2])

# #list is mutable==>we can change existing element
# l=[10,20,30,40]
# l[1]=100
# print(l)

# #len number
# l=[100,500,300,"shubham"]
# print(len(l))

#add element into the list
#append() method add number one by one
# l=[]
# l.append(4)
# l.append(7)
# l.append([40,50])
# print(l)

# #extend() add the number into the list whole,extend work only with iteratable
# a=[1,2,3,4,5]
# b=[6,7,8,9,10]
# a.append(b)#append b ek list me enter kr deta h 
# b.extend(a)
# print(a)
# print(b)

#insert the value in list using index value
l=[10,30,60,35,89]
l.insert(4,56) #(index,value)
print(l)

#remove()   and pop()
l=[10,20,30,40,50,60,70]
l.remove(30) #remove method remove the value and pop use index value to remove value
print(l)

a=[10,40,50,70,20,90]
a.pop(2) # 2 is th eindex value and by default value last element pop return krta h value
print(a)
#remove() return the null value
#pop () return the value

# clear() the value
# if u want a list but clear all the value use clear method
l=[30,50,70,90]
l.clear()
print(l)

#del method puri variable tak ko dlete kr deta h memory se
k=[5,6,7,8,9,0]
del k[0] # 5 is delete into list
print(k) #k is delete