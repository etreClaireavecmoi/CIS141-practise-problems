# 1. Prompt the user for a word. Then, prompt the user for how many times they'd 
#like that word repeated. Use the skills you learned in this module to print the 
#word the correct number of times.

word = input("Give me a word: ")
repeat = input("How many times would you like this word to be repeated? ")
repeat = int(repeat)
print(word * repeat)
