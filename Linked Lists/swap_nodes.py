# Swap Nodes in Pairs

"""
Example: 24. Swap Nodes in Pairs

Given the head of a linked list, swap every pair of nodes.
For example, given a linked list 1 -> 2 -> 3 -> 4 -> 5 -> 6, return a linked list 2 -> 1 -> 4 -> 3 -> 6 -> 5.
"""

"""
Again, let's break down what we need to do step by step, and how we can accomplish it. Consider the first pair of nodes as A -> B.

1. Starting with head at node A, we need node B to point here.
    We can accomplish this by doing head.next.next = head

2. However, if we change B.next, we will lose access to the rest of the list.
    Before applying the change in step 1, save a pointer nextNode = head.next.next.


head.next.next is used differently in steps 1 and 2. When it is before the assignment operator (=), it is changing head.next's next node.
When it is after the assignment, it is referring to head.next's next node.

"""

"""

1. We now have B pointing at A. We need to move on to the next pair C, D. However, A is still pointing at B, which isn't what we want.
   If we move on to the next pair immediately, we will lose a reference to A, and won't be able to change A.next.

    Save A in another pointer with prev = head (we haven't changed head yet so it's still pointing at A).
    To move to the next pair, do head = nextNode.

2. Once we move on to the next pair C -> D, we need A to point to D.

    Now that head is at C, and prev is at A, we can do prev.next = head.next.

3. The first pair A, B is fully completed. B points to A and A points to D. When we started, we had head pointing to A.
After going through steps 1 - 4, we completed A, B. Right now, we have head pointing to C.
If we go through the steps again, we will have complete C, D, and be ready for the next pair.
We can just repeat steps 1 - 4 until all pairs are swapped. But what do we return at the end?

    Once all the pairs are finished, we need to return B. Unfortunately, we lost the reference to B a long time ago.
    We can fix this by saving B in a dummy node before starting the algorithm.



4. What if there is an odd number of nodes? In step 4, we set A.next to C.next. What if there were only 3 nodes, so C.next was null?

    Before moving on to the next pair, set head.next = nextNode. This is setting A.next to C.
    Note that this effect will be overridden by step 4 in the next swap if there is still a pair of nodes remaining.
    Since in step 2 we do head.next.next, we need our while loop condition to check for both head and head.next.
    That means if there is only one node left in the list, the while loop will end after the current iteration. As such, this effect wouldn't be overridden.
    For example, consider the list A -> B -> C -> D. At some point, we have B <-> A C -> D. Here, we perform step 6, and we get B -> A -> C -> D.
    When we start swapping the pair C, D, step 4 will set A.next to D, which overrides what we just did with step 6.
    But if D didn't exist, then the iteration would have just ended. In that scenario, we would have B -> A -> C, which is what we want.

"""

"""

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # Check edge case: linked list has 0 or 1 nodes, just return
        if not head or not head.next:
            return head

        dummy = head.next               # Step 5
        prev = None                     # Initialize for step 3
        while head and head.next:
            if prev:
                prev.next = head.next   # Step 4
            prev = head                 # Step 3

            next_node = head.next.next  # Step 2
            head.next.next = head       # Step 1

            head.next = next_node       # Step 6
            head = next_node            # Move to next pair (Step 3)

        return dummy
"""

# My solution


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        if not head.next:
            return head

        dummy = ListNode(0, head)

        prev = dummy

        while head and head.next:

            first = head
            second = head.next

            first.next = second.next
            second.next = first
            prev.next = second

            prev = first
            head = first.next
        return dummy.next

