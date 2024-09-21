# Backspace String Compare

"""
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.


Example 1:

Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".

Example 2:

Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".

Example 3:

Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".


Constraints:

    1 <= s.length, t.length <= 200
    s and t only contain lowercase letters and '#' characters.

Follow up: Can you solve it in O(n) time and O(1) space?
"""

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # I will use two stacks
        # I will iterate through both strings. If we run into a '#' we pop the top of the stack
        # At the end we will compare both stacks for equality

        s_stack = []
        t_stack = []

        for char in s:
            if char != '#':
                s_stack.append(char)
            elif s_stack:
                s_stack.pop()

        for char in t:
            if char != '#':
                t_stack.append(char)
            elif t_stack:
                t_stack.pop()

        return t_stack == s_stack


# Follow up solution - Two pointer solution

class Solution(object):
    def backspaceCompare(self, S, T):
        def F(S):
            skip = 0
            for x in reversed(S):
                if x == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield x

        return all(x == y for x, y in itertools.izip_longest(F(S), F(T)))