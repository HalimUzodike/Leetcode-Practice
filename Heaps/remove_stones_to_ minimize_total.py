# Remove Stones to Minimize the Total

"""
You are given a 0-indexed integer array piles, where piles[i] represents the number of stones in the ith pile, and an integer k.
You should apply the following operation exactly k times:

    Choose any piles[i] and remove floor(piles[i] / 2) stones from it.

Notice that you can apply the operation on the same pile more than once.

Return the minimum possible total number of stones remaining after applying the k operations.

floor(x) is the greatest integer that is smaller than or equal to x (i.e., rounds x down).
"""

"""
Example 1:

Input: piles = [5,4,9], k = 2
Output: 12
Explanation: Steps of a possible scenario are:
- Apply the operation on pile 2. The resulting piles are [5,4,5].
- Apply the operation on pile 0. The resulting piles are [3,4,5].
The total number of stones in [3,4,5] is 12.

Example 2:

Input: piles = [4,3,6,7], k = 3
Output: 12
Explanation: Steps of a possible scenario are:
- Apply the operation on pile 2. The resulting piles are [4,3,3,7].
- Apply the operation on pile 3. The resulting piles are [4,3,3,4].
- Apply the operation on pile 0. The resulting piles are [2,3,3,4].
The total number of stones in [2,3,3,4] is 12.


Constraints:
    1 <= piles.length <= 105
    1 <= piles[i] <= 104
    1 <= k <= 105
"""


from heapq import *
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        # use a max heap to get the pile, since we are minimizing the total
        # we will subtract floor(piles[i] / 2) from the max value.
        # We will add the result back to the heap.
        # We will then subtract 1 from k at the end of each loop.
        # We will exit the loop and return the result (the sum of the piles) when k = 0

        piles = [-stone for stone in piles]
        heapify(piles)

        while k > 0:
            sub = piles[0]
            maximum = heappop(piles)
            result = -maximum - (-sub // 2)
            heappush(piles, -result)
            k = k - 1
        
        final = abs(sum(piles))
        return final
        