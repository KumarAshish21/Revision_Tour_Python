# 9.9. Generators¶

# Genrators are a simple and powerful tool for creating iterators. They are written like regular functions but use the yield statement whenever they want to return data.
# Each time next() is called on it, the genrators resumes where it left off.
def reverse(data):
    for index in range(len(data)-1,-1,-1):
        yield data[index]
        
for char in reverse('golf'):
    print(char)
    
    
