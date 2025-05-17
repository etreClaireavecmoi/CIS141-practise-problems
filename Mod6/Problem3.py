#3. Create a list of strings. Write code to create a new list that includes only 
#the strings <longer than> three characters. Print the resulting filtered list.

finnquotes = ['Sup', 'Mathmatical!', 'Algebraic!', 'Eh', 'Hey Jake!', 'That armour is totally chk-chk!', 'nah']
newlist = []
for i in finnquotes:
    if len(i) > 3:
        newlist.append(i)
print(newlist)

