#slicing the list
l=[10,20,30,40,50,60,44,88,22,11]
print(l[2:8:2])# 30,50,44
print(l[8:2:-2])#22,44,50,30
print(l[-2:-8:-2])#22,44,50,30
print(l[-8:-2:2])#30,50,44
print(l[-1:-7:-2])#11,88,60,
print(l[2:-2:2])#30,50,44
print(l[5:1])#[]
print(l[1:5:-1])#[]
print(l[-1:-5])#[]
print(l[::])#10,20,30,40,50,60,44,88,22,11
print(l[9:1:-3])#11,44,40
print(l[-2:2:1])#[]
print(l[-8:-4:1])#30,40,50,60,44

#negative index is not equal to negative direction
#negative step is equal to negative direction like right to left

# #isko krne ke rule h 
# start
# end
# step 
# agr step negative h to right to left chlan h fir start me aur end jo marji ho
# agr step postive h to left to right chlna h fir start se end tak bus