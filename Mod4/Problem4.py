#4. A theater wants to enforce age restrictions for movie tickets. 
#Ask the user for their age, and tell them whether they can see G (appropriate for under 13), 
#PG-13 (appropriate for 13 to 17), or R (appropriate for over 18) rated movies.
age = int(input("Quel âge avez-vous ? ")) #What age are you?
if age >= 18:
    print("fèlicitations; vous pouvez regarde ce que vous voulez ! Ce serait 15 euros maintenant, merci. ") #Congratulations, you can watch whatever you want! That will be 15 euros now, thanks.
elif age >= 13 and age <= 17:
    print("Désolé, vous ne pouvez regarder que des films classés G ou PG-13.") #Sorry, you can only watch G or PG-13 films.
else:
    print("Désolé, mais tu ne peux regarder que des films classés G. Où sont tes parents ? ") #Sorry, but you can only watch G rated films. Where are your parents?
