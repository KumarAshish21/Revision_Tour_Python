# Longest Common Prefix
# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string "".
# Example 1:
#
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:
#
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

def longest_common_prefix(strs):
    if not strs:
        return ""
    shortest = min(strs,key=len)
    for i, ch in enumerate(shortest):
        for other in strs:
            if other[i] != ch:
                return shortest[:i]
    return shortest
strs = ["flower","flow","flight"]
print(longest_common_prefix(strs))

def longest_common_prefix(strs):
    if not strs:
        return ""
    for i in range(len(strs[0])):
        for string in strs[1:]:
            if i >= len(string) or string[i] != strs[0][i]:
                return strs[0][:i]
    return strs[0]
strs = ["flower","flow","flight"]
print(longest_common_prefix(strs))

def longest_common_prefix(strs):
    if not strs:
        return ""
    s1 = min(strs)
    s2 = max(strs)
    for i, c in enumerate(s1):
        if c != s2[i]:
            return s1[:i]
    return s1
strs = ["flower","flow","flight"]
print(longest_common_prefix(strs))

def longest_common_prefix(strs):
    if not strs:
        return ""
    prefix = strs[0]
    for string in strs:
        while string.find(prefix) != 0:
            prefix = prefix[:len(prefix)-1]
            if not prefix:
                return ""
    return prefix
strs = ["flower","flow","flight"]
print(longest_common_prefix(strs))

