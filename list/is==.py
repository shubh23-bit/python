a=[1,2,3,4]
b=[1,2,3,4]
print(a==b)#true value checking
print(a is b)#false  because inka object alg h reference alg h


c=[1,2,3,4]
d=c #assign hona mtlb same refernce ban rah ah
c.append(10)
print(c==d)#true
print( c is d)#true