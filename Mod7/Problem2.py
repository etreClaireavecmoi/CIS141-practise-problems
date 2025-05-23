#2. Write a function called is_palindrome(s) that checks 
#whether a string is a palindrome, ignoring case. .lower
#The function should <return> either True or False. bool

#radar, racecar, Radar, seven

def is_palindrome(s):
    s = s.lower()
    if s == s[::-1]:
        return True
    else:
        return False

print(is_palindrome("radar"))
print(is_palindrome("Radar"))
print(is_palindrome("Racecar"))
print(is_palindrome("seven"))
