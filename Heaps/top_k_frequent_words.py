# Top K Frequent Words

"""
Given an array of strings words and an integer k, return the k most frequent strings.

Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order.


Example 1:

Input: words = ["i","love","leetcode","i","love","coding"], k = 2
Output: ["i","love"]
Explanation: "i" and "love" are the two most frequent words.
Note that "i" comes before "love" due to a lower alphabetical order.

Example 2:

Input: words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4
Output: ["the","is","sunny","day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words, with the number of occurrence being 4, 3, 2 and 1 respectively.

"""

"""
Constraints:

    1 <= words.length <= 500
    1 <= words[i].length <= 10
    words[i] consists of lowercase English letters.
    k is in the range [1, The number of unique words[i]]

Follow-up: Could you solve it in O(n log(k)) time and O(n) extra space?
"""


# Uses Max heap

# Time - O(n*logk)
# Space - O(n)

from heapq import *
from collections import Counter

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        counter = Counter(words)
        heap = [(-frequency, word) for word, frequency in counter.items()] # Get the heap ready
        heapify(heap) # Create the heap
        
        solution = []
        for _ in range(k):
            if heap:
                solution.append(heappop(heap)[1])
        
        # You can also use the following for the solution
        # solution = [heappop(heap)[1] for _ in range(k)]
        
        return solution


# Alternative solution
# Uses Max heap

# Time - O(n*logk)
# Space - O(n)

from heapq import *
from collections import Counter

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        counter = Counter(words)
        heap = [(-frequency, word) for word, frequency in counter.items()] # Get the heap ready
        heapify(heap) # Create the heap

        solution = []
        while len(solution) < k:
            if heap:
                solution.append(heappop(heap)[1])
        
        # You can also use the following for the solution
        # solution = [heappop(heap)[1] for _ in range(k)]
        
        return solution

        