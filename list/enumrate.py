#enumrate hame index value deta h
#list ke sath index +value milti h
a=[1,2,3,4,5,6]
print(list(enumerate(a)))

for i ,x in enumerate(a):
    print(i,x)

s = ["A", "B", "C"]

print(list(enumerate(s, start=5)))#start ka use ham isley krte h ki index value ham us value se start krt skate h