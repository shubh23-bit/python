a=[[1,2],[3,4]]
b=a.copy()
b[0].append(5)
print(a) #5 ist list me add ho jyega a me bhi or b me bhi becuse copy sirf outerlist hoga
print(b)
print(a is b)
#Because copy() ne sirf outer list ka copy banaya.
c=[1,2,3,4,5]
d=c
print( c is d)


#deepcopy ka use krenge agr a and b alg alg cheya
import copy
a=[[1,2,3,4],[1,2,3,4,5]]
b=copy.deepcopy(a)
b[0].append(100)
print(a)
print(b)
print(a is b)