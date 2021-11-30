dict={}
n1=int(input("Enter the number of elements in dict"))
for i in range(0,n1):
   k=input("Enter the key")
   v=input("Enter the value")
   dict[k]=v
print(dict)
print("The dictionary sorted in ascending order")
print(sorted(dict.items()))
print("The dictionary sorted in descending order")
print(sorted(dict.items(),reverse=1))
