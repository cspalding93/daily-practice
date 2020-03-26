# the prompt
"""
Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

move_zeros([false,1,0,1,2,0,1,3,"a"]) # returns[false,1,1,2,1,3,"a",0,0]
"""
# my solution

def move_zeros(array):
    start = []
    end = []
    for i, x in enumerate(array):
        if type(x) == type(0.0):
            x = int(x)
        if type(x) != type(42) or x != 0:
            start.append(x)
        else:
            end.append(x)
    return start+end

# time complexity: O(n)
# space complexity: O(2)

"""
The highest rated response:

def move_zeros(arr):
    l = [i for i in arr if isinstance(i, bool) or i!=0]
    return l+[0]*(len(arr)-len(l))
    
Response: really clever filter method that simplifies the code
"""