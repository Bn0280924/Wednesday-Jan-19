a=0
s=input("What is the word you want to find out if it is even or odd ")
for c in s:
    print(c)
    print(ord(c))
    
    b=ord(c)
    a=a+b
print(a)
if (a % 2)==0:
    print("Num is even")
else:
    print("Num is odd")
    