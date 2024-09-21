# Week 2: Arrays and Strings. Two pointers

# mutable arr = ["a", "b", "c"]
# immutable string = "abc"

# Two pointer technique - First method

# Initialize the left pointer at 0 and the right pointer at input.length - 1

# You can swap positions using list[left], list[right] = list[right], list[left]

# Example 1
def check_if_palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True


# Example 2
def check_for_target(nums, target):
    """
    This algorithm uses O(1) space and time complexity of O(n)
    :param nums:
    :param target:
    :return:
    """
    left = 0
    right = len(nums) - 1

    while left < right:
        # curr is the current sum
        curr = nums[left] + nums[right]
        if curr == target:
            return True
        if curr > target:
            right -= 1
        else:
            left += 1

    return False


# Two pointer technique - Second method

# Example 3
def combine(arr1, arr2):
    # ans is the answer
    ans = []
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            ans.append(arr1[i])
            i += 1
        else:
            ans.append(arr2[j])
            j += 1

    # You need these while loops to make sure both lists have been exhausted
    while i < len(arr1):
        ans.append(arr1[i])
        i += 1

    while j < len(arr2):
        ans.append(arr2[j])
        j += 1

    return ans


# Example 4
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1

        return i == len(s)



#  --------------------------------------------------------Sliding window technique


# A sliding window is a data structure that keeps track of a "view" of a list over a given interval.


# If the logic done for each operation is O(1), then the overall runtime complexity is O(n).

# When to use a sliding window?


# First, the problem will either explicitly or implicitly define criteria that
# make a subarray "valid". There are 2 components regarding what makes a subarray valid:

# 1. A constraint metric. This is some attribute of a subarray.
#    It could be the sum, the number of unique elements, the frequency
#    of a specific element, or any other attribute.
# 2. A numeric restriction on the constraint metric.
#    This is what the constraint metric should be for a subarray to be considered valid.

# For example, let's say a problem declares a subarray is valid if it has a sum
# less than or equal to 10. The constraint metric here is the sum of the subarray,
# and the numeric restriction is <= 10. A subarray is considered valid
# if its constraint metric conforms to the numeric restriction,
# i.e. the sum is less than or equal to 10.

# Second, the problem will ask you to find valid subarrays in some way.

# - The most common task you will see is finding the best valid subarray.
#   The problem will define what makes a subarray better than another.
#   For example, a problem might ask you to find the longest valid subarray.

# - Another common task is finding the number of valid subarrays.
#   We will take a look at this later in the article.


# Dynamic Sliding Window Technique

# Example 1: Given an array of positive integers nums and an integer k, find the length of the longest subarray whose sum is less than or equal to k.

# Plan: Use two pointers - left and right. While the sum of elements in the window is less than or equal to k, keep expanding the window.
#       Keep track of the maximum length of the valid window.
#       Move the right pointer forward if the sum is less than or equal to k.
#       Move the left pointer forward if the sum is greater than k.



# nums = [3, 1, 2, 7, 4, 2, 1, 1, 5]
# k = 8
# Answer should be 4 for this example

def max_subarray_sum(nums, k):

    current_sum = 0
    left = 0  # left pointer
    answer = 0

    for right in range(len(nums)):
        current_sum += nums[right]
        while current_sum > k:
            current_sum -= nums[left]
            left += 1
        if current_sum <= k:
            answer = max(answer, right - left + 1)

    return answer

# print(max_subarray_sum(nums, k))


# Example 2: You are given a binary string s (a string containing only "0" and "1"). You may choose up to one "0" and flip it to a "1".
#            What is the length of the longest substring achievable that contains only "1"?
#            For example, given s = "1101100111", the answer is 5. If you perform the flip at index 2, the string becomes 1111100111


# Plan: Use two pointers - left and right. While the substring contains only "1", keep expanding the window.
#       Keep track of the maximum length of the valid window.
#       Move the right pointer forward if the substring contains only "1".
#       Move the left pointer forward if the substring contains only "0".

def max_subarray_sum_binary(s):

    # curr is the current number of zeros in the window
    left = curr = ans = 0
    for right in range(len(s)):
        if s[right] == "0":
            curr += 1
        while curr > 1:
            if s[left] == "0":
                curr -= 1
            left += 1
        ans = max(ans, right - left + 1)

    return ans

# print(max_subarray_sum_binary(s))



# Fixed size sliding window


# In the examples we looked at above, our window size was dynamic.
# We tried to expand it to the right as much as we could while keeping the window within some constraint
# and removed elements from the left when the constraint was violated. Sometimes, a problem will specify a fixed length k.

# These problems are easy because the difference between any two adjacent windows is only two elements
# (we add one element on the right and remove one element on the left to maintain the length).

# Start by building the first window (from index 0 to k - 1).
# Once we have a window of size k, if we add an element at index i, we need to remove the element at index i - k.
# For example, k = 2 and you currently have elements at indices [0, 1]. Now, we add 2: [0, 1, 2].
# To keep the window size at k = 2, we need to remove 2 - k = 0: [1, 2].


# Example 4: Given an integer array nums and an integer k, find the sum of the subarray with the largest sum whose length is k.

# As we mentioned before, we can build a window of length k and then slide it along the array.
# Add and remove one element at a time to make sure the window stays size k. If we are adding the value at i, then we need to remove the value at i - k.
# After we build the first window we initialize our answer to curr to consider the first window's sum.

# The total for loop iterations is equal to nn, where nn is the length of nums, and the work done in each iteration is constant,
# giving this algorithm a time complexity of O(n), using O(1) space.

def find_best_subarray(nums, k):
    curr = 0
    for i in range(k):
        curr += nums[i]

    ans = curr
    for i in range(k, len(nums)):
        curr += nums[i] - nums[i - k]
        ans = max(ans, curr)

    return ans




#  --------------------------------------------------------Prefix Sums


"""
Prefix sum is a technique that can be used on arrays (of numbers).
The idea is to create an array prefix where prefix[i] is the sum of all elements up to the index i (inclusive).
For example, given nums = [5, 2, 1, 6, 3, 8], we would have prefix = [5, 7, 8, 14, 17, 25]


When a subarray starts at index 0, it is considered a "prefix" of the array. A prefix sum represents the sum of all prefixes.

Prefix sums allow us to find the sum of any subarray in O(1).
If we want the sum of the subarray from i to j (inclusive),
then the answer is prefix[j] - prefix[i - 1], or prefix[j] - prefix[i] + nums[i] if you don't want to deal with the out of bounds case when i = 0.

This works because prefix[i - 1] is the sum of all elements before index i.
When you subtract this from the sum of all elements up to index j, you are left with the sum of all elements starting at index i and ending at index j,
which is exactly what we are looking for.
"""


"""
Building a prefix sum is very simple. Here's some pseudocode:

Given an array nums,

prefix = [nums[0]]
for (int i = 1; i < nums.length; i++)
    prefix.append(nums[i] + prefix[prefix.length - 1])

Initially, we start with just the first element.
Then we iterate with i starting from index 1. At any given point,
the last element of prefix will represent the sum of all the elements in the input up to but not including index i.
So we can add that value plus the current value to the end of prefix and continue to the next element.

A prefix sum is a great tool whenever a problem involves sums of a subarray.
It only costs O(n) to build but allows all future subarray queries to be O(1)O(1),
so it can usually improve an algorithm's time complexity by a factor of O(n)O(n), where nn is the length of the array. Let's look at some examples.
"""



"""

Example 1: Given an integer array nums, an array queries where queries[i] = [x, y] and an integer limit,
return a boolean array that represents the answer to each query. A query is true if the sum of the subarray from x to y is less than limit, or false otherwise.

For example, given nums = [1, 6, 3, 2, 7, 2], queries = [[0, 3], [2, 5], [2, 4]], and limit = 13,
the answer is [true, false, true]. For each query, the subarray sums are [12, 14, 12].

"""

def answer_queries(nums, queries, limit):
    prefix = [nums[0]]
    for i in range(1, len(nums)):
        prefix.append(nums[i] + prefix[-1])  # Append the sum of the current element and the current last element of prefix

    ans = []
    for x, y in queries:
        curr = prefix[y] - prefix[x] + nums[x]
        ans.append(curr < limit)

    return ans


#  Prefix example using strings

"""
Longest Common Prefix


Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".


Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.


Constraints:
    1 <= strs.length <= 200
    0 <= strs[i].length <= 200
    strs[i] consists of only lowercase English letters.
"""


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if not len(strs):
            return ""

        prefix = strs[0]
        for i in range(1, len(strs)):
            while strs[i].find(prefix) != 0:
                prefix = prefix[0 : len(prefix) - 1]
                if prefix == "":
                    return ""
        return prefix
