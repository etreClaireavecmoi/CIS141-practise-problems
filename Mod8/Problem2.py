#2. Write a Python program that allows users to log their hiking trips. The program
#should:
#- Use a while loop to repeatedly ask for a hike name and distance in miles
#- Save each entry to hiking_log.txt (each hike on a new line)
#- When the user presses 0, exit the loop & print the <contents of hiking_log.txt>

while True:
    hike = input('Where did you hike? (0 to exit): ')
    if hike == '0':
        break
    miles = input('In miles, how long was the trek? (0 to exit): ')
    if miles == '0':
        break
    with open('hiking_log.txt', 'a') as file:
        file.write(f'Your hike at {hike} was {miles} miles long.\n')
        print(f'Saved! Your hike at {hike} was {miles} miles long.\n')
print('\nHere is what has been recorded to date:')
with open('hiking_log.txt', 'r') as file:
    for line in file: 
        print(line)
        
