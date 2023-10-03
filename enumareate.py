sports = ['cricket','kabbaddi','tennis','badminton']
enum_obj = enumerate(sports,start=1)
print(type(enum_obj))
print(list(enum_obj))

# where use function

for pos,ele in enumerate(sports): #[(pos,ele)]
    print(f"{pos}:{ele}")

# conversion to dictionary

print(dict(list(enumerate(sports,1)))) #[(cnt,data1),(),()]

# conversion to json

import json
sports = ['cricket','kabbaddi','tennis','badminton']
data= dict(list(enumerate(sports,1)))

with open('data.json','w') as file:
    json.dump(data,file)
