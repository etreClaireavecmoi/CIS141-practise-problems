#3. Prompt the user for their bank balance. Evaluate whether the balance is less than $100. 
#Print True if the user’s balance is below $100; print False, otherwise.

breakeven = 100 #I tried break and breakpoint, but apperantly those are both recognised by python lol.
bal = int(input("What is your account's current balance? "))
if bal < breakeven:
    print("True")
else: bal >= breakeven
print("False")
