# Valid Parenthesis

"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.


Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

Constraints:
    1 <= s.length <= 104
    s consists of parentheses only '()[]{}'.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        # Use a stack.
        # I will build a hashmap 'store' with the open brac as keys and closed as values
        # As we go through the string if we encounter open bracs we add them to the stack
        # If we encounter a closed bracket and its corres isn't at the top of the stack we ret False
        # If the closed bracs corres is at the top of the stack we pop it.
        # If we reach the end of the string and the stack is not empty we return False
        # Return True if at the end of the string and the stack is empty

        stack = []
        store = {'(': ')', '[':']', '{':'}'}

        for char in s:
            if char in store:
                stack.append(char)

            elif char not in store and not stack or char != store[stack[-1]]:
                return False

            else:
                stack.pop()

        return True if not stack else False