# s = "geek"
# var = ""
# for i in s:
#     var = i + var
# print(var)

# print(s[::-1])

# Check of rotation

def arrrotations(s1,s2):
    if len(s1) != len(s2):
        return False
    temp = ' '
    temp = s1 + s2
    return temp.find(s2) != -1
s1 = "ASHI"
s2 = "IHSA"
print(arrrotations(s1,s2))