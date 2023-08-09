 # Given list
List = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
 
# Empty list
ansList = []
 
for num in List :
     
    # 0 and 1 is not a  prime number
    if num == 0 or num == 1 :
        continue
        
    for i in range(2, num // 2 + 1) :
 
        # If number is divisible by any  number (i) then it is not a prime number
        if num % i == 0 :
            break
 
    # If not divisible then it is  a prime number
    else :
         
    
        ansList.append(num)
 
# If list is non-empty then print the elements
if len(ansList) :
     
    print("Prime Number : ",end = "-> ")
     
    # printing the prime number from the ansList
    for ans in ansList :
        print(ans, end = ", ")
     
else :
    print("No any number from the given list is Prime")
