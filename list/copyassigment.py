# copy() vs assigment

a=[10,20,30,40]
b=a
a=[10,20,30,40]
print(a)
print(b)
# a and b dono ek hi list ko refer kr rahe h ye important h

b=a.copy()#copy kya krt ah ek nayi list create kr deta h to isley b me jo chneg kia wo a me nhi aya

b.append(40)
print(a)
print(b)