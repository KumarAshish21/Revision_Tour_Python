"""
Approach #1 : Using stack One approach to check balanced parentheses is to use stack. Each time, when an open parentheses is encountered push it in the stack, and when closed parenthesis is encountered, match it with the top of stack and pop it. If stack is empty at the end, return Balanced otherwise, Unbalanced. 
"""
open_list = ["[","{","("]
close_list = ["]","}",")"]


def check(myStr):
    stack = []
    for i in myStr:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if ((len(stack) > 0) and (open_list[pos] == stack[len(stack)-1])):
                stack.pop()

            else:
                return "Unbalanced"
        
    if len(stack) == 0:
        return "Balanced"
    else:
        return "Unbalanced"
    

string = "{[]{()}}"
print(string,"-", check(string))

string = "[{}{})(]"
print(string,"-",check(string))

string = "((()"
print(string,"-",check(string))


"""
Approach #2 : Using queue First Map opening parentheses to respective closing parentheses. Iterate through the given expression using 'i', if 'i' is an open parentheses, append in queue, if 'i' is close parentheses, Check whether queue is empty or 'i' is the top element of queue, if yes, return "Unbalanced", otherwise "Balanced". 
"""
def check(expression):
    open_tup = tuple('({[')
    close_tup = tuple(')}]')
    map =dict(zip(open_tup, close_tup))
    queue = []

    for i in expression:
        if i in open_tup:
            queue.append(map[i])

        elif i in close_tup:
            if not queue or i != queue.pop():
                return "Unbalanced"
            
    
    if not queue:
        return "Balanced"
    else:
        "Unbalanced"

string = "{[]{()}}"
print(string, "-", check(string))

string = "((()"
print(string,"-",check(string))



"""
Approach#3 : Elimination based In every iteration, the innermost brackets get eliminated (replaced with empty string). If we end up with an empty string, our initial one was balanced; otherwise, not. 
"""

def check(my_string):
    brackets = ['()','{}','[]']
    while any(x in my_string for x in brackets):
        for br in brackets:
            my_string = my_string.replace(br, '')

    return not my_string

string = "{[]{()}}";
print(string, "-", "Balanced" 
      if check(string) else "Unbalanced")