"""
A regular expression (or RE) specifies a set of strings that matches it; the functions in this module let you check if a particular string matches a given regular expression (or if a given regular expression matches a particular string, which comes down to the same thing).
"""


import re
s = 'set of strings that matches it the functions in this module let you check'
match = re.search(r'functions',s)
print('Start Index',match.start())
print('End Index:',match.end())