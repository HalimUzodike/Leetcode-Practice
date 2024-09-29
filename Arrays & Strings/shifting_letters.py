# Shifting Letters

"""
You are given a string s of lowercase English letters and an integer array shifts of the same length.

Call the shift() of a letter, the next letter in the alphabet, (wrapping around so that 'z' becomes 'a').

    For example, shift('a') = 'b', shift('t') = 'u', and shift('z') = 'a'.

Now for each shifts[i] = x, we want to shift the first i + 1 letters of s, x times.

Return the final string after all such shifts to s are applied.



Example 1:

Input: s = "abc", shifts = [3,5,9]
Output: "rpl"
Explanation: We start with "abc".
After shifting the first 1 letters of s by 3, we have "dbc".
After shifting the first 2 letters of s by 5, we have "igc".
After shifting the first 3 letters of s by 9, we have "rpl", the answer.

Example 2:

Input: s = "aaa", shifts = [1,2,3]
Output: "gfd"

"""

class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        # Initialize an empty list to store the shifted characters
        ans = []

        # Calculate the total shift (modulo 26 to handle wrap-around)
        total_shifts = sum(shifts) % 26

        # Iterate through each character in the string and its index
        for i, c in enumerate(s):
            # Convert the character to its 0-based index in the alphabet
            index = ord(c) - ord('a')

            # Shift the character and append to the answer list
            # The modulo 26 ensures we stay within the alphabet
            ans.append(chr(ord('a') + (index + total_shifts) % 26))

            # Update X for the next iteration
            # Subtract the current shift and take modulo 26
            total_shifts = (total_shifts - shifts[i])

        # Join the list of shifted characters into a string and return
        return "".join(ans)