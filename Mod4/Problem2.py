#2. The headlights of a car should only automatically turn on when the daylight outside 
#is below a certain threshold. If a sensor threshold is below the number 8, print "Headlights On"; 
#otherwise, print "Headlights Off".

sensor = 8
number = int(input("Current sensor readout is: "))
if number < sensor:
    print("Headlights on.")
else: 
    print("Headlights off.")
