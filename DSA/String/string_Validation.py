import re

def validate(s):
    # Check length
    if len(s) < 10:
        return False
    
    # Check for at least 1 numeric character
    if not any(char.isdigit() for char in s):
        return False
    
    # Check for at least 1 uppercase character
    if not any(char.isupper() for char in s):
        return False
        
    # Check for at least 1 lowercase character
    if not any(char.islower() for char in s):
        return False
        
    # Check for at least 1 special character from @#$-*
    special_characters = set('@#$-*')
    if not any(char in special_characters for char in s):
        return False
    
    # If all conditions are met, the string is valid
    return True

# Example usage:
password = "eHello123@"
if validate(password):
    print("String is valid.")
else:
    print("String is not valid.")


# Panagram
def isPanagram(s):
    unique_char = set()
    for char in s:
        if char.isalpha():
            unique_char.add(char.lower())
    return len(unique_char) == 26
s = "Thequickbrownfoxjumpsoverthelazydog"
print(isPanagram(s))

# Missing Characters in Panagrami

def missingPanagram(s):
    unique_char = set()
    for i in s:
        if i.isalpha():
            unique_char.add(i.lower())
    letter = set('Abcdefghijklmnopqrstuvwxyz')
    missing_letters = sorted(letter - unique_char)
    
    result = ''.join(missing_letters)
            
    return result
s = 'Abc'
print(missingPanagram(s))

def missingPanagram(s):
    letters = "abcdefghijklmnopqrstuvwxyz"
    ab = ""
    for i in letters:
        if i not in s.lower():
            ab += i
    if ab == "":
        return -1
    else:
        return ab
            
s = 'Abcdefghijklmnopqrstuvwxy'
print(missingPanagram(s))


