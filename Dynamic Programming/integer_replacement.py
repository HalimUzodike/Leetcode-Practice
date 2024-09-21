# Integer Replacement

"""
Given a positive integer n, you can apply one of the following operations:

    If n is even, replace n with n / 2.
    If n is odd, replace n with either n + 1 or n - 1.

Return the minimum number of operations needed for n to become 1. 

Example 1:

Input: n = 8
Output: 3
Explanation: 8 -> 4 -> 2 -> 1

Example 2:

Input: n = 7
Output: 4
Explanation: 7 -> 8 -> 4 -> 2 -> 1
or 7 -> 6 -> 3 -> 2 -> 1

Example 3:

Input: n = 4
Output: 2

Constraints:
    1 <= n <= 231 - 1

"""

# Solutions

# Time - O(logn)
# Space - O(logn)

class Solution:
    def integerReplacement(self, n: int) -> int:
        
        def helper(n, total):
            if n == 1:
                return total
            
            if n % 2 == 0:
                total += 1
                return helper(n/2, total)
            
            else:
                total += 1
                return min(helper(n + 1, total),helper(n - 1, total))
        # total = 0  # Could use this instead of putting the raw 0 in the helper fucntion tbh
        return helper(n, 0)



# With memoization - Dynamic Programming
# Time - O(logn)
# Space - O(logn)

class Solution:
    def integerReplacement(self, n: int) -> int:
        
        def helper(n):

            memo = {0:0, 1:0}

            if n in memo:
                return memo[n]
            
            if n % 2 == 0:
                memo[n] = helper(n/2) + 1
            
            else:
                memo[n] = min(helper(n + 1), helper(n - 1)) + 1

            return memo[n]

        return helper(n)



# With memoization and functools lru_cache - Dynamic Programming
# Time - O(logn)
# Space - O(logn)

from functools import lru_cache

class Solution:
    def integerReplacement(self, n: int) -> int:

        @lru_cache
        def helper(n):
            if n <= 1:
                return 0
            if n % 2 == 0:
                return helper(n / 2) + 1
            else:
                return min(helper(n + 1), helper(n - 1)) + 1
        
        return helper(n)