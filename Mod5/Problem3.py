#3. Use a for loop and the range() function to print all 
#even numbers from 2 to 20.

'''
for i in range(2, 21, 2):
    print(i)
'''

for i in range(2, 21):
    if i % 2 == 0:
        print(i)
    else:
        continue
        
#I made a second one incase first using step was cheap. 
