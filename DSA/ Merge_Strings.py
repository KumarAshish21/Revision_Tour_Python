#  Merge Strings Alternately

# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

# Return the merged string.



word1 = "abc"
word2 = "pqr"
arr1 = ""
min_length = min(len(word1),len(word2))
for i in range(min_length):
    arr1 += word1[i] + word2[i]
arr1+= word1[min_length:] + word2[min_length:]
print(arr1)

def mergeAlternately(word1,word2):
    min_len = min(len(word1), len(word2))
    merged = [word1[i] + word2[i] for i in range(min_len)]
    return ''.join(merged) + word1[min_len:] + word2[min_len:]
word1 = "abc"
word2 = "pqr"
print(mergeAlternately(word1,word2))