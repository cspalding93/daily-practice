"""
Clock shows 'h' hours, 'm' minutes and 's' seconds after midnight.

Your task is to make 'Past' function which returns time converted to milliseconds.

Example:
past(0, 1, 1) == 61000
Input constraints: 0 <= h <= 23, 0 <= m <= 59, 0 <= s <= 59
"""

def past(h, m, s):
    h *= 60**2
    m *= 60
    return (h+m+s)*1000

# time complexity: O(1)

"""
# most upvoted answer on the site

def past(h, m, s):
    return (3600*h + 60*m + s) * 1000
"""

# my answer is not a single line, but I prefer the more explicit style \
# since there is going to be little to no difference in space complexity