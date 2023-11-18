def multiply(*args):
    print(args)
    total = 1
    for arg in args:
        total = total * arg
    return total
    
print(multiply(1,3,5))


def apply(*args, operator):
    if operator == "*":
        return multiply(*args)
    elif operator == "+":
        return sum(args)
    
    else:
        return "NO vaild operator provided to apply()."
    
print(apply(1, 3, 6, 7, operator="+"))



def names(**kwargs):
    print(kwargs)
names(name ="Ashish", ages = 25)

