#1.count the characxter
s="shubham bisht"
count=0
for ch in s:
    count=count+1
print(count)
################################################################
s = "programming"
count=0
for ch in s:
    #print(ch)
    if ch=="g":
        count=count+1
print(count)
##############################################################
# reverse the string
s="python"
rev=""
for ch in s:
     rev=ch+rev
print(rev)
##################################################
#palindrome
s="madam"
rev=""
for ch in s:
     rev=ch+rev

if rev==s:
    print("palindrome")
else:
    print("not palindrome")


#########################################################
#count vowels
s="hello world shubham "
count=""


