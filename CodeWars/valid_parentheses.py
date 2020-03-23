# the prompt
"""
Write a function called that takes a string of parentheses, and determines if the order of the parentheses is valid. The function should return true if the string is valid, and false if it's invalid.

Examples
"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true
Constraints
0 <= input.length <= 100

Along with opening (() and closing ()) parenthesis, input may contain any valid ASCII characters. Furthermore, the input string may be empty and/or not contain any parentheses at all. Do not treat other forms of brackets as parentheses (e.g. [], {}, <>).
"""
# the solution I arrived at:
def valid_parentheses(string):
    paren = []
    
    for p in string:
        if p in set( ["(", ")"] ):         # sort of a quick filter for the parentheses to reduce time if possible 
            if not len(paren):             # starts the list if it is empty
                paren.append( p )
            else:
                if p == ")":               # checks for closing parentheses only
                    if paren[-1] == "(":   # validation of complete parentheses
                        paren.pop(-1)      
                    else:                  # adds to or removes items from the list
                        paren.append(p)
                else:
                    paren.append(p)        # appends all instances of opening brackets
                    
    answer = bool( len( paren ) )          # converts the length of the paren list to a bool
    return not answer                      # returns appropriate bool


# time complexity: O(n)
# space complexity: O(1)

"""
This is the highest rated solution:


def valid_parentheses(string):
    cnt = 0
    for char in string:
        if char == '(': cnt += 1
        if char == ')': cnt -= 1
        if cnt < 0: return False
    return True if cnt == 0 else False
"""    
    