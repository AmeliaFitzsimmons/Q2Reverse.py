s = input("Enter your word, for it to be reversed:")

reversedString=[]
index = len(s) # calculate length of string and save in index
while index > 0:
  reversedString += s[ index - 1 ] # save the value of str[index-1] in reverseString
  index = index - 1 # decrement index
print(reversedString) # reversed string