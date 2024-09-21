#  Stack


"""
A stack is an ordered collection of elements where elements are only added and removed from the same end.
In the physical world, an example of a stack would be a stack of plates in a kitchen - you add plates or remove plates from the top of the pile.
In the software world, a good example of a stack is the history of your current browser's tab.
Let's say you're on site A, and you click on a link to go to site B, then from B you click on another link to go to site C.
Every time you click a link, you are adding to the stack - your history is now [A, B, C].
When you click the back arrow, you are "removing" from the stack - click it once and you have [A, B], click it again and you have [A].
"""

"""
Interface guide for stacks:

# Declaration: we will just use a list
stack = []

# Pushing elements:
stack.append(1)
stack.append(2)
stack.append(3)

# Popping elements:
stack.pop() # 3
stack.pop() # 2

# Check if empty
not stack # False

# Check element at top
stack[-1] # 1

# Get size
len(stack) # 1
"""