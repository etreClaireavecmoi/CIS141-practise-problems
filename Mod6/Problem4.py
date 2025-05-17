#4.  Create a list of integers. Write code that counts how many numbers are positive 
#and how many are negative, then print both counts.

liste = [-1,-2,-3,0,1,2,3,4,5]
nega = []
posi = []
for i in liste:
    if i > 0:
        posi.append(i)
    elif i < 0:
        nega.append(i)
print('Original list:', liste)
print()
print('Positives in the original list: ', posi)
print()
print('Negatives in the original list: ', nega)
