# Next Greater Element

"""
The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.

You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.

Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.



Example 1:

Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
- 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
- 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.

Example 2:

Input: nums1 = [2,4], nums2 = [1,2,3,4]
Output: [3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 2 is underlined in nums2 = [1,2,3,4]. The next greater element is 3.
- 4 is underlined in nums2 = [1,2,3,4]. There is no next greater element, so the answer is -1.


Constraints:

    1 <= nums1.length <= nums2.length <= 1000
    0 <= nums1[i], nums2[i] <= 104
    All integers in nums1 and nums2 are unique.
    All the integers of nums1 also appear in nums2.

Follow up: Could you find an O(nums1.length + nums2.length) solution?
"""



class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Init a stack and hashmap(store). Monotonic decreasing stack.
        # For each num in nums, if the stack is not empty and num is greater that the top of
        #   the stack. We will pop and add the  val at the popped number to the hasmap as the
        #   key and the greater number as the value.
        # If num is less than stack[-1], then we will simply append the number to the stack
        # If the stack is not empty after this, then it means that there are no greater values
        #   in the nums2 array, this means that we will pop the remaining into the hashmap with
        #   a value of -1 representing that nothing is greater
        # We then return an array containing the next greatest element for each number in nums1
        # We will use a store.get(i, -1) with -1 as the default if the element in nums1 is not
        #   a key in the store

        stack = []
        store = {}

        for num in nums2:
            while stack and num > stack[-1]:
                store[stack.pop()] = num
            stack.append(num)

        while stack:
            store[stack.pop()] = -1

        return [store.get(i, -1) for i in nums1]
