#lambda argument :expression
#normal function
def square(a):
    print(a*a)
square(4)

#lambda function

square=lambda x:x*x
print(square(4))

# lambda       → keyword
# x            → input/parameter
# :            → separates input and logic
# x * 2        → expression/result

check=lambda x:"even" if x%2==0 else "odd"
print(check(4))

f = lambda x: x + 10

a = f(5)
b = f(a)

print(a)
print(b)

########################################################################
students=[
    ("aman",80),
    ("rahul",50),
    ("gaurav",90)
]
students.sort(key=lambda x:x[1])
print(students)

students.sort(key=lambda x:x[1],reverse=True)
print(students)