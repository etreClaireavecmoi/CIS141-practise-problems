#5. Write a function called level_up(experience) that takes a player's experience
#points and returns their new level based on these rules:
#* 0-99 XP → Level 1
#* 100-199 XP → Level 2
#* 200+ XP → Level 3

def level_up(experience):
    if experience <= 99:
        return "You are currently level 1."
    elif experience >= 100 and experience < 200:
        return "You are currently level 2."
    else:
        return "You are currently level 3."

print(level_up(41))
print(level_up(100))
print(level_up(199))
print(level_up(200))
