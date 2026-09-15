#reverse() vs reversed()
a=[10,20,30,40]
x=a.reverse()
print(a)
print(x) #reverse bhi none return krata h sort ki trah and remove ki ki trah and orginal a ko reverse krdeta h

x=reversed(a)
print(x)

y=list(reversed(a))
print(y)