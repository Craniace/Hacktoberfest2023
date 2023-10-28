#Program to Display unique vowels using stack
vowels=['a','e','i','o','u']
word=input("Enter the word:")
stack=[]
for letter in word:
    if letter in vowels:
        if letter not in stack:
            stack.append(letter)
print(stack)
print("The number of different vowels present in",word,"is",len(stack))




