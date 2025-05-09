#5. Write a program that continuously asks the user to input a number. 
#If the user enters 0, immediately stop asking for more numbers. 
#Otherwise, print the number they entered.

n = int(input("Enter a number! (Type 0 to end program): "))
while n != 0:
    print(f"You've entered {n}.")
    n = int(input("Enter another number. (Type 0 to end program): "))
else:
    print("Exiting...")
    
