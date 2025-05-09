#1. Prompt the user for a positive integer n. 
#Use a while loop to sum all the integers from 1 up to n. 
#Print the final sum.

count = 1 
total = 0
n = int(input("Give me a positive whole number: "))
while count <= n:
    total = count + total
    count += 1
print(total)
