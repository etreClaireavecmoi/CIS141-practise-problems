#5. Create a list of integers. Use a loop to build a new list where each element is 
#the square of the corresponding element in the original list. Print the new list.
liste = [1,2,3,4,5,6]
deuxiemeliste = [] 
for i in liste:
    deuxiemeliste.append(i * i)
print('The original list: ', liste)
print('The numbers from the original list, squared: ', deuxiemeliste)
