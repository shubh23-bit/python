# sort() vs sorted()
a=[50,10,2,45,76]#sort original list ko modify kr deta h
x=a.sort() #sort into ascending order
print(a)
print(x)

#desending order ke liy
a.sort(reverse=True)
print(a)

b=sorted(a)
print(b)#sorted orginal list same rakhta h new list bna ke value ko sort kr deta h

#sort() → original list change + returns None

#sorted() → original list same + returns new sorted list#