# Basic Calculator I, II & III


"""
Basic Calculator I

Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().



Example 1:

Input: s = "1 + 1"
Output: 2

Example 2:

Input: s = " 2-1 + 2 "
Output: 3

Example 3:

Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23


Constraints:

    1 <= s.length <= 3 * 105
    s consists of digits, '+', '-', '(', ')', and ' '.
    s represents a valid expression.
    '+' is not used as a unary operation (i.e., "+1" and "+(2 + 3)" is invalid).
    '-' could be used as a unary operation (i.e., "-1" and "-(2 + 3)" is valid).
    There will be no two consecutive operators in the input.
    Every number and running calculation will fit in a signed 32-bit integer.

"""

"""
Recursive Solution

class Solution:
    def calculate(self, s):
        def evaluate(i):
            res, digit, sign = 0, 0, 1

            while i < len(s):
                if s[i].isdigit():
                    digit = digit * 10 + int(s[i])
                elif s[i] in '+-':
                    res += digit * sign
                    digit = 0
                    sign = 1 if s[i] == '+' else -1
                elif s[i] == '(':
                    subres, i = evaluate(i+1)
                    res += sign * subres
                elif s[i] == ')':
                    res += digit * sign
                    return res, i
                i += 1

            return res + digit * sign

        return evaluate(0)

"""

def calculate(self, s: str) -> int:
    """
    1. Take 3 containers:
    num -> to store current num value only
    sign -> to store sign value, initially +1
    res -> to store sum
    When ( comes these containers used for calculate sum of intergers within () brackets.
    --------------------
    2. When c is + or -
    Move num to res, because we need to empty num for next integer value.
    set num = 0
    sign = update with c
    --------------------
    3. When c is '('
    Here, we need num, res, sign to calculate sum of integers within ()
    So, move num and sign to stack => [num, sign]
    Now reset - res = 0, num = 0, sign = 1 (default)
    --------------------
    4. When c is ')' -> 2-(3+4), Here res=3, num=4, sign=1 stack [2, -]
    res +=sign*num -> calculate sum for num first, then pop items from stack, res=7
    res *=stack.pop() - > Pop sign(+ or -) to multiply with res, res = 7*(-1)
    res +=stack.pop() - > Pop integer and add with prev. sum, res = -7 + 2 - 5
    --------------------
    Simple Example: 2 - 3
    Initially res will have 2,i.e. res = 2
    then store '-' in sign. it will be used when 3 comes. ie. sign = -1
    Now 3 comes => res = res + num*sign
    Return statement: res+num*sign => res = 2 + 3(-1) = 2 - 3 = -1
    """
    num = 0
    sign = 1
    res = 0
    stack = []
    for i in range(len(s)): # iterate till last character
        c = s[i]
        if c.isdigit(): # process if there is digit
            num = num * 10 + int(c) # for consecutive digits 98 => 9x10 + 8 = 98
        elif c in '-+': # check for - and +
            res += num * sign
            sign = -1 if c == '-' else 1
            num = 0
        elif c == '(':
            stack.append(res)
            stack.append(sign)
            res = 0
            sign = 1
        elif c == ')':
            res += sign * num
            res *= stack.pop()
            res += stack.pop()
            num = 0
    return res + num * sign




"""
Basic Calculator II

Given a string s which represents an expression, evaluate this expression and return its value.

The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().



Example 1:

Input: s = "3+2*2"
Output: 7

Example 2:

Input: s = " 3/2 "
Output: 1

Example 3:

Input: s = " 3+5 / 2 "
Output: 5



Constraints:

    1 <= s.length <= 3 * 105
    s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
    s represents a valid expression.
    All the integers in the expression are non-negative integers in the range [0, 231 - 1].
    The answer is guaranteed to fit in a 32-bit integer.

"""

class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        prev_operator = '+'

        for i in range(len(s) + 1):
            ch = s[i] if i < len(s) else '\0'

            if ch.isdigit():
                num = num * 10 + int(ch)

            if not ch.isdigit() and ch != ' ' or i == len(s):
                if prev_operator == '+':
                    stack.append(num)
                if prev_operator == '-':
                    stack.append(-num)
                if prev_operator == '*':
                    stack.append(stack.pop() * num)
                if prev_operator == '/':
                    stack.append(int(stack.pop() / num))

                prev_operator = ch
                num = 0

        return sum(stack)



"""
Basic Calculator III


Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, '+', '-', '*', '/' operators, and open '(' and closing parentheses ')'.
The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().



Example 1:

Input: s = "1+1"
Output: 2

Example 2:

Input: s = "6-4/2"
Output: 4

Example 3:

Input: s = "2*(5+5*2)/3+(6/2+8)"
Output: 21


Constraints:

    1 <= s <= 104
    s consists of digits, '+', '-', '*', '/', '(', and ')'.
    s is a valid expression.

"""


class Solution:
    def calculate(self, s: str) -> int:
        it = 0

        def calc() -> int:
            nonlocal it
            def update(op: str, v: int) -> None:
                if op == "+": stack.append(v)
                if op == "-": stack.append(-v)
                if op == "*": stack.append(stack.pop() * v)
                if op == "/": stack.append(int(stack.pop() / v))

            num, stack, sign = 0, [], "+"

            while it < len(s):
                if s[it].isdigit():
                    num = num * 10 + int(s[it])
                elif s[it] in "+-*/":
                    update(sign, num)
                    num, sign = 0, s[it]
                elif s[it] == "(":
                    it += 1
                    num = calc()
                elif s[it] == ")":
                    update(sign, num)
                    return sum(stack)
                it += 1
            update(sign, num)
            return sum(stack)

        return calc()



"""
Most Inuitive Solution for the basic calculator problems

https://leetcode.com/problems/basic-calculator-iii/solutions/3844828/python-3-pattern-for-basic-calculator-i-ii-ii/

def calculate(self, s: str) -> int:
    it = 0

    def calc() -> int:
        nonlocal it
        def update(op: str, v: int) -> None:
            if op == "+": stack.append(v)
            if op == "-": stack.append(-v)
            if op == "*": stack.append(stack.pop() * v)
            if op == "/": stack.append(int(stack.pop() / v))

        num, stack, sign = 0, [], "+"

        while it < len(s):
            if s[it].isdigit():
                num = num * 10 + int(s[it])
            elif s[it] in "+-*/":
                update(sign, num)
                num, sign = 0, s[it]
            elif s[it] == "(":
                it += 1
                num = calc()
            elif s[it] == ")":
                update(sign, num)
                return sum(stack)
            it += 1
        update(sign, num)
        return sum(stack)

    return calc()
"""