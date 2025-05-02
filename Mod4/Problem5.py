#5. A store charges $5 for shipping on any order under $50. 
#If the order amount is $50 or more, shipping is free. 
#Ask the user for the order total and print the total cost, including shipping.

subtotal = float(input("What was the cost of your order? "))
if subtotal >= 50.00:
    print(f"Congratulations, you've earned free shipping! Your total cost is {subtotal:.2f}")
else: 
    print(f"Unfortunately, your order does not qualify for free shipping. Your total cost is {subtotal + 5:.2f}")
