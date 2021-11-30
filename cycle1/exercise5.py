a=input("Enter the list of values")
b=input("Enter the list of values")
c=a.split()
d=b.split()
l1=list(map(int,c))
l2=list(map(int,d))
if len(l1)==len(l2):
  print("Lists are of same length")
else:
   print("Lists are of different length")
sum1=0
for i in range(0,len(l1)):
   sum1=sum1 + l1[i]
print("Sum of values in first list:",sum1)        
sum2=0   
for j in range(0,len(l2)):
    sum2=sum2 + l2[j]
print("Sum of values in second list:",sum2)        
if sum1==sum2:
    print("The List sums upto same value ")
else:
    print("The sums of the lists are different")
for i in range(0,len(l2)):
  if(l1[i] in l2):
    print("This value occurs in both the list:",l1[i])
