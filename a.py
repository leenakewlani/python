a=[10,50,60,70,80]
print(a)
temp=a.pop()
c=a[0]
a.append(c)
a[0]=temp
print(a)
print(c)

