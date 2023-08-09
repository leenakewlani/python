input_list=input("enter your string")
word_list=input_list.split()
print("the word list :",word_list)
result= [word for word in word_list if len(word)>=2 and word[0] == word[-1]]
print("after seperating the same words:",result)
