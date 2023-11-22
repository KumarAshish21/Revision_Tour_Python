# Python program to print the first non-repeating character

NO_OF_CHARS = 256

def getCharCountArray(string):
	count = [0] * NO_OF_CHARS
	for i in string:
		count[ord(i)]+= 1
	return count

def firstNonRepeating(string):
	count = getCharCountArray(string)
	index = -1
	k = 0

	for i in string:
		if count[ord(i)] == 1:
			index = k
			break
		k += 1

	return index

string = "geeksforgeeks"
index = firstNonRepeating(string)
if index == 1:
	print ("Either all characters are repeating or string is empty")
else:
	print ("First non-repeating character is" , string[index])



# Leftmost Non-Repeating Element
# Naive

import sys
CHAR = 256
def nonrep(st) :
    fi = [-1] * CHAR 
    for i in range(len(st)) :
        if fi[ord(st[i])] == -1 :
            fi[ord(st[i])] = i
        else :
            fi[ord(st[i])] = -2 
    res = sys.maxsize
    for i in range(CHAR) :
        if fi[i] >= 0 :
            res = min(res,fi[i])
    if res == sys.maxsize :
        return -1
    else :
        return res 
    
    
st = "apple"
print(nonrep(st))