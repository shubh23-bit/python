# filter bcially to filter out the value from th elist
a=[1,2,3,4,5,6,7] #filter out the even numbe in the list
x=[i for i in a if i%2==0]
print(x)


a = [1, 2, 3, 4, 5]

result = list(filter(lambda x: x > 3, a))

print(result)