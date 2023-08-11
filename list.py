a=['ritivik','isha','rita','aaina']
b=input("enter your name")
print(b)
choice=int(input("enter your choice:1.show list\n2.add your name \n3.delete your name"))

if choice==1:
    if b in a:
        print(a)
        print("enter 3 if you want to delete your name")
    else:
        print("your name is not there in the list")
        print("enter 2 to add your name")
        choice=int(input("enter your choice:1.show list\n2.add your name \n3.delete your name"))

if choice==2:
    a.append(b)
    print(a)
    choice=int(input("enter your choice:1.show list\n2.add your name \n3.delete your name"))
if choice==3:
    d=input("enter the name you want to delete")
    a.remove(d)
    print(a)
    
else:
    print('exit')
        
