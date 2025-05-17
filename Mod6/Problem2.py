#2. Create a list of strings. Write code that counts how many times the word "Olympic" appears 
#in the list, and then print the count.
threads = ['wool', 'cotton', 'hemp', 'nylon', 'olympic composites']
count = 0
for i in threads:
    if 'olympic' in i.lower():
        count += 1
print(threads)
print('Given this list, "Olympic" appears', count, 'time(s).')
print()
olys = ['Olympia', 'The Olympics', 'Olympic Mountain Range', 'Mount Olympus', 'Olympians']
olycount = 0
for j in olys:
    if 'olympic' in j.lower():
        olycount += 1
print(olys)
print('Given this list, "Olympic" appears', olycount, 'time(s).')
