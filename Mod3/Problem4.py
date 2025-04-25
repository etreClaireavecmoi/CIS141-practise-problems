#4. Prompt the user for: a word, a first index, and a last index.
#Slice the word at the indexes provided by the user and print to the screen.

word = input("Give me a word: ")
index1 = int(input("Give me an index: "))
index2 = int(input("Give me a second index: "))

print(f"Given the word and indexing you gave, the result is: {word[index1:index2]}.")

