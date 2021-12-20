a=int(input("Enter the number"))
n=a
s=0
while n!=0:
    r=n%10
    s=s+(r*r*r)
    n=n//10
    
if s==a:
    print("The number %d is Armstrong",s)

else:
     print("The number %d is not Armstrong",s)

