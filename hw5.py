num=int(input("enter number"))
sum=0
temp=num
while num>0:
    rem=num%10
    sum=sum*10+rem
    num=num//10
if (temp==sum):
    print("its a palindrome")

else:
    print("its not a palindrome")
    
