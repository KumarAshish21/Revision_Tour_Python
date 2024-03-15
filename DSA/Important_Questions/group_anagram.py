# Group Anagrams
# Given an array of strings, group anagrams together. You can return the answer in any order.
# An Analgram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Example:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Input: strs = [""]
# Output: [[""]]

# Input: strs = ["a"]
# Output: [["a"]]

def groupAnagrams(strs):
    result = {}
    for s in strs:
        sorted_str = ''.join(sorted(s))
        if sorted_str in result:
            result[sorted_str].append(s)
        else:
            result[sorted_str] = [s]
    return list(result.values())
print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

# Method 2 using Hashmap
def groupAnagrams(strs):
    result = {}
    for s in strs:
        count = [0]*26
        for c in s:
            count[ord(c)-ord('a')] += 1
        if tuple(count) in result:
            result[tuple(count)].append(s)
        else:
            result[tuple(count)] = [s]
    return list(result.values())
print(groupAnagrams([""]))

