a=input("enter the list")
b=map(int,a.split())
c=[i for i in b if i %2 != 0]
print(c)
