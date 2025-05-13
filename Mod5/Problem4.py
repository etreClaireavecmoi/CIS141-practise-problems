#4. Use nested for loops to create a simple multiplication table for 
#numbers 1 through 5. Format your output so that each row corresponds 
#to multiplying by a specific number. 
#Example output (See cis141-mod 5 practise problems for the table.)

for i in range(1,6):
    for j in range(1,6):
        print(i * j, end="\t ")
    print(" ")
#I don't understand how to get the spacing to look like your solution
#example, would you mind letting me know how to fix this? 
#each 2 digit number shifts the table. 
