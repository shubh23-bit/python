#list searching and counting
a=[10,20,30,40,50]
print(10 in a)
print(40 not in a)
print(100 in a)
b=["python","ajay","rahul"]
print("python" in b)
print("py" in b) #in pura word check krta h check krta h
#in is case sensetive
print('Python' in a)#shoukd be false beacuse of case senstivite

# index find the index of value

c=[10,20,30,40,50,60,20,20]
print(c.index(30)) #2 because the value of 30 in index of 2
#and alwayts return first occurance
#if value not exit in any index then give value error
#print(c.index(100))

# count() method is use to how many time value is present in list
print(c.count(20))
print(c.count(100))#if value not present then 0 will print


