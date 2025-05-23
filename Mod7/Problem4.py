#4. Write a function called ferry_fare(age, vehicle) that calculates the Washington
#State Ferry fare based on <age> <and> whether the person <has a vehicle.> Assume the following rates:
# Adults (19-64): $10 without a vehicle, $20 with a vehicle.
# Seniors (65+): $5 without a vehicle, $15 with a vehicle.
# Children (0-18): Free.

def ferry_fare(age, vehicle):
    vehicle = vehicle.lower()
    if age >= 65 and vehicle == "yes":
        return "Your cost today is 15.00$" 
    elif age >= 65 and vehicle == "no":
        return "Your cost today is 5.00$"
    elif age >= 19 and age < 65 and vehicle == "yes":
        return "Your cost today is 20.00$"
    elif age >= 19 and age < 65 and vehicle == "no":
        return "Your cost today is 10.00$"
    else:
        return "Your cost today is 0.00$"

print(ferry_fare(72, "yes"))
print(ferry_fare(72, "no"))
print()
print(ferry_fare(41, "yes"))
print(ferry_fare(39, "NO"))
print()
print(ferry_fare(12, 'no'))
print(ferry_fare(17, "YES"))
