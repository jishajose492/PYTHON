s1=input("Enter First string : ")
s2=input("Enter Second string : ")
x=s1[0:1]
s1=s1.replace(s1[0:1],s2[0:1])
s2=s2.replace(s2[0:1],x)
print(s1+" "+s2)
