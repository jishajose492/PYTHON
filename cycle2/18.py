a=int(input("Enter the number"))
c=0
for i in range(2,a):
    if (a%i)==0:
        c=c+1
if c>0:
    print("The Number" ,a, "is not prime")
else:print("The Number" ,a,  "is prime")    
