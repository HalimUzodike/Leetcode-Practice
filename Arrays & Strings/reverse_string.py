class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        left, right = 0, len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right += -1

        return None

# For future reference to remember that the increment/decrement part can also be written as
# left, right = left + 1, right - 1
