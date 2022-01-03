a=input("Enter the list")
l=map(int,a.split())
newlist=[x for x in l if x >=0]
print(newlist)
