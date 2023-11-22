s1= input("Enter a String:\n")
s2= input("Enter a String:\n")

def areAnagram(s1,s2):
    if len(s1) != len(s2):
        return False
    s1=sorted(s1)
    s2=sorted(s2)
    return(s1==s2)


s1= input("Enter a String:\n"
s2= input("Enter a String:\n")

def areAnagram(s1,s2):
    if len(s1) != len(s2):
        return False
    count=[0]*256
    for i in range(len(s1)):
        count[ord(s1[i])]+=1
        count[ord(s2[i])]-=1
    for x in count:
        if x!=0:
            return False
    return True

#  

# There are four different ways to perform string formatting in Python:
# Formatting with % Operator.
# Formatting with format() string method.
# Formatting with string literals, called f-strings.
# Formatting with String Template Class