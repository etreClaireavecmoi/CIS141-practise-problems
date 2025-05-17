#1. Create a list of integers (you get to pick!). 
#Write code to iterate through the list and calculate the sum of all even numbers. 
#Print the resulting sum.
liste = [1,4,2,5,8,5,8,6,4,2]
sumevens = []
print(liste)
for evens in liste:
    if evens %2 == 0:
        sumevens.append(evens)
print("The even digits from the above list: ", sumevens)
print("The sum of all evens in the list is: ", sum(sumevens))
