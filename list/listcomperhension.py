#list comperhension
#print number 1 to 5
x=[]
for i in range(1,6):
    x.append(i)
print(x)

x=[i for i in range(1,6)]
print(x)

#find square
x=[i*i for i in range(1,6)]
print(x)
# find even number
c=[1,2,3,4,5,6,7,8]
a=[i for i in c if i%2==0]
print(a)

a=[1,2,3,4,5,6]
b=[x if x%2==0 else 0 for x in a]
print(b)