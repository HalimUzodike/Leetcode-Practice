# Linked Lists - Two


"""
Reverse a linked list

While reversing a linked list is a common interview problem in itself, it is also a technique that can be a step in solving different problems.
Elegantly performing the reversal requires a good understanding of how to move pointers around, which we will aim to achieve in this article.

Imagine that we have a linked list 1 -> 2 -> 3 -> 4, and we want to return 4 -> 3 -> 2 -> 1.
Let's say we keep a pointer curr that represents the current node we are at. Starting with curr at the 1, we need to get the 2 to point to curr.
The problem is, once we iterate (curr = curr.next) to get to the 2, we no longer have a pointer to the 1 because it is a singly linked list.
To get around this, we can use another pointer prev that tracks the previous node.

At any given node curr, we can set curr.next = prev to switch the direction of the arrow.
Then, we can update prev to be curr in preparation for the next node. However, if we change curr.next, we will lose that next node.
To fix this, we can use a temporary variable nextNode to point to the next node before changing any of the other pointers.
"""

def reverse_list(head):
    prev = None
    curr = head
    while curr:
        next_node = curr.next # first, make sure we don't lose the next node
        curr.next = prev      # reverse the direction of the pointer
        prev = curr           # set the current node to prev for the next node
        curr = next_node      # move on

    return prev

# Another approach for reversing a linked list (with python)

def reverse_linked_list(head):
    curr, prev = head, None
    while curr:
        curr.next, prev, curr = prev, curr, curr.next
    return prev



"""
Reverse linked list II

Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.


Example 1:
Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]

Example 2:

Input: head = [5], left = 1, right = 1
Output: [5]

"""

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head

        dummy = ListNode(0, head)
        prev = dummy

        # Find the node just before the reversal starts
        for _ in range(left - 1):
            prev = prev.next

        start = prev.next
        end = start

        # Find the end of the sublist to be reversed
        for _ in range(right - left):
            end = end.next

        # Save the part after the reversed section
        next_part = end.next

        # Cut the sublist to be reversed
        end.next = None

        # Reverse the sublist
        reversed_part = self.reverse(start)

        # Connect the reversed part back to the list
        prev.next = reversed_part
        start.next = next_part

        return dummy.next

    def reverse(self, node: Optional[ListNode]) -> Optional[ListNode]:
        if not node:
            return None

        prev, curr = None, node

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev