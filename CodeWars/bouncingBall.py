# the prompt:
"""
A child is playing with a ball on the nth floor of a tall building. The height of this floor, h, is known.

He drops the ball out of the window. The ball bounces (for example), to two-thirds of its height (a bounce of 0.66).

His mother looks out of a window 1.5 meters from the ground.

How many times will the mother see the ball pass in front of her window (including when it's falling and bouncing?

Three conditions must be met for a valid experiment:
Float parameter "h" in meters must be greater than 0
Float parameter "bounce" must be greater than 0 and less than 1
Float parameter "window" must be less than h.
If all three conditions above are fulfilled, return a positive integer, otherwise return -1.

Note:
The ball can only be seen if the height of the rebounding ball is strictly greater than the window parameter.

Example:

```
- h = 3, bounce = 0.66, window = 1.5, result is 3

- h = 3, bounce = 1, window = 1.5, result is -1 

(Condition 2) not fulfilled).
```

"""

# the solution I first arrived at
def bouncingBall(h, bounce, window):
    conditions = sum( [ (h > 0), ( (bounce > 0) & (bounce < 1) ), (window < h) ] )
    if conditions != 3:
        return -1
    else: 
        ball_h = h
        seen = 0
        while ball_h > window:
            # falling
            seen += 1
            # bouncing
            ball_h *= bounce
            # rising
            if ball_h > window:
                seen += 1
        return seen
# time complexity: O(1)
# space complexity: O(1)    

    
""" 
This is the highest rated answer so far

def bouncingBall(h, bounce, window):
    if not 0 < bounce < 1: return -1
    count = 0
    while h > window:
        count += 1
        h *= bounce
        if h > window: count += 1
    return count or -1
    
"""