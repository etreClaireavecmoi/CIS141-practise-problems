#3. In the game Pokemon, certain types of Pokemon do extra damage 
#to other types. E.g. water is very effective to fight fire.

#Write a function called type_advantage(attacker, defender) 
#that takes two Pokémon types as strings and returns 
#"Super Effective", "Not Very Effective", or "Neutral" 
#based on simple type effectiveness rules. 
#Your solution only needs to work for these three sets of input:
#print(type_advantage("Water", "Fire")) # "Super Effective"
#print(type_advantage("Fire", "Water")) # "Not Very Effective"
#print(type_advantage("Electric", "Grass")) # "Neutral"

def type_advantage(attacker, defender):
    
    if attacker.lower() == "water" and defender.lower() == "fire":
        return "It's Super Effective!"
    elif attacker.lower() == "fire" and defender.lower() == "water":
        return "It's not very effective..."
    elif attacker.lower() == "electric" and defender.lower() == "grass":
        return "neutral"

print(f"Squirtle used Bubble Beam on Charmander. \n{type_advantage('Water', 'Fire')}")
print()
print(f"Charmander used Flare on Squirtle. \n{type_advantage('Fire', 'Water')}")
print()
print("Squirtle fainted!")
print()
print("Choose a Pokémon.")
print("Go! Pikachu!")
print()
print("Gary withdrew Charmander!")
print("Go! Bulbasaur!")
print()
print(f"Pikachu used Static Electricity on Bulbasaur, it's {type_advantage('electric', 'Grass')}.")
print()
print("Bulbasaur used Dig!")
