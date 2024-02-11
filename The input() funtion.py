print("Tell me anything...")
anything = input()
print("Hmm...", anything, "... Really?")

anything = input("Tell me anything...")
print("Hmm...", anything, "...Really?")\

#Result of the input() function is a string.
anything = input("Enter a number: ")
something = anything ** 2.0 #TypeError (string ** ) !!!! 
print(anything, "to the power of 2 is", something)