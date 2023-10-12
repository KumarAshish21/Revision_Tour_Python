# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.


def reverseVowels(s):
    vowels = (['a','e','i','o','u','A','E','I','O','U'])
    s = list(s)
    left,right = 0,len(s)-1
    while left<right:
        while left < right and s[left] not in vowels:
            left +=1
        while left < right and s[right] not in vowels:
            right -= 1
        
        s[left], s[right] = s[right], s[left]
        left +=1
        right -= 1
    return ''.join(s)
s = "leetcode"
print(reverseVowels(s))

print(0<0)