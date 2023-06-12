"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false


"""


def isAnagram(s, t):
    if len(s)!= len(t):
        return False
    
    countS, countT = {},{}
    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i],0)
        countT[t[i]] = 1 + countT.get(t[i],0)

    for c in countS:
        if countS[c] != countT.get(c,0):
            return False
    return True
s = input()
t = input()
print(isAnagram(s, t))