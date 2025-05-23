#1. Write a <function called count_vowels(input)> that takes a 
#string and <returns> the <number> of vowels (a, e, i, o, u) in it.
    
def count_vowels(inputs):
    count = 0
    inputs = inputs.lower()
    vowel = "aiueo"
    for letter in inputs:
        if letter in vowel:
            count += 1
        else:
            continue
    return count

print(f"There are {count_vowels('Apples')} vowels in this word.")
print(count_vowels("apples"))
print(count_vowels("Pomme de terre")) #spaces still don't count as vowels
