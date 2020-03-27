# the prompt:
"""
Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !

"""
# My solution:

def pig_it(text):
    human = text.split()
    pig = []
    for word in human:
        if len(word) > 1 and word.isalnum():
            pig.append(word[1:]+word[0]+"ay")
        elif word.isalnum():
            pig.append(word+"ay")
        else:
            pig.append(word)
    return " ".join(pig)
    
# time complexity: O(n)
# space complexity: O(1)
"""
the highest rated response:

def pig_it(text):
    lst = text.split()
    return ' '.join( [word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])
    
This is a really impressive use of list comprehension I would have loved to natrually gone to this solution
"""