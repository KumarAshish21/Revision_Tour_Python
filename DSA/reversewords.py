# Reverse words in string
# s = "the sky is blue"
# s ="  hello world  "
s = "a good   example"
lit =[]
stri = ""
for i in s:
    if i != " ":
        stri += i
    elif stri != "":
        lit.append(stri)
        stri = ""
if stri!="":
    lit.append(stri)
a = " ".join(lit[::-1])
print(a)
        
    