# prompt
"""
Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.

Examples input/output:

XO("ooxx") => true
XO("xooxx") => false
XO("ooxXm") => true
XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
XO("zzoo") => false

"""

# my response

def xo(s):
    s = s.lower()
    count = 0
    for c in s:
        if c == 'o': count += 1
        if c == 'x': count -= 1
        
    return not bool( count )

# time complexity: O(n)
# space complexity: O(1)

"""
the highest rated answer 

def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')
"""
# I wanted to avoid the count feature, but that is actually much simpler in retrospect