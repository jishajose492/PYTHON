dict1={}
dict2={}
n1=int(input("Enter the number of elements in first dict"))
n2=int(input("Enter the number of elements in second dict"))
for i in range(0,n1):
   k=input("Enter the key")
   v=input("Enter the value")
   dict1[k]=v
print(dict1)
for i in range(0,n2):
   k=input("Enter the key")
   v=input("Enter the value")
   dict2[k]=v
print(dict2)
for key in dict1:
 if key in dict2:
   dict2[key] += dict1[key]
 else:
   pass
dict1.update(dict2)
print("The merged dictionary is:",dict2)
 
