numbers=input("enter the numbers").split()
print(numbers)
palindrome=[num for num in numbers if num==num[::-1]]
print(palindrome)
intpalindrome = list(map(int,palindrome))
print(intpalindrome)

