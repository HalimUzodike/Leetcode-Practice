# Linked Lists


"""
A linked list is a data structure that is similar to an array.
It also stores data in an ordered manner, but it is implemented using node objects (you will have a custom class that defines the node object).
Each node will have a "next" pointer, which points to the node representing the next element in the sequence.
"""


# Singly Linked List

"""
Singly linked list

This is the most common type of linked list and the one that is given in the code above. In a singly linked list, each node only has a pointer to the next node.
This means you can only move forward in the list when iterating. The pointer used to reference the next node is usually called next.

Let's say you want to add an element to a linked list so that it becomes the element at position i.
To do this, you need to have a pointer to the element currently at position i - 1.
The next element (currently at position i), call it x, will be pushed to the element at position i + 1 after the insertion.
This means that x should become the next node to the one being added, and the node being added should become the next node to the one currently at i - 1.
Here's some code and images demonstrating:
"""

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

# Let prev_node be the node at position i - 1
def add_node(prev_node, node_to_add):
    node_to_add.next = prev_node.next
    prev_node.next = node_to_add


# Let prev_node be the node at position i - 1
def delete_node(prev_node):
    prev_node.next = prev_node.next.next


# Doubly Linked List

"""
Doubly linked list

A doubly linked list is like a singly linked list, but each node also contains a pointer to the previous node. This pointer is usually called prev, and it allows iteration in both directions.

In a singly linked list, we needed a reference to the node at i - 1 if we wanted to add or remove at i. This is because we needed to perform operations on the prevNode. With a doubly linked list, we only need a reference to the node at i. This is because we can simply reference the prev pointer of that node to get the node at i - 1, and then do the exact same operations as above.

With a doubly linked list, we need to do extra work to also update the prev pointers.
"""

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

# Let node be the node at position i
def add_node(node, node_to_add):
    prev_node = node.prev
    node_to_add.next = node
    node_to_add.prev = prev_node
    prev_node.next = node_to_add
    node.prev = node_to_add

# Let node be the node at position i
def delete_node(node):
    prev_node = node.prev
    next_node = node.next
    prev_node.next = next_node
    next_node.prev = prev_node




# Linked Lists with sentinel nodes

"""
Linked lists with sentinel nodes

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

def add_to_end(node_to_add):
    node_to_add.next = tail
    node_to_add.prev = tail.prev
    tail.prev.next = node_to_add
    tail.prev = node_to_add

def remove_from_end():
    if head.next == tail:
        return

    node_to_remove = tail.prev
    node_to_remove.prev.next = tail
    tail.prev = node_to_remove.prev

def add_to_start(node_to_add):
    node_to_add.prev = head
    node_to_add.next = head.next
    head.next.prev = node_to_add
    head.next = node_to_add

def remove_from_start():
    if head.next == tail:
        return

    node_to_remove = head.next
    node_to_remove.next.prev = head
    head.next = node_to_remove.next

head = ListNode(None)
tail = ListNode(None)
head.next = tail
tail.prev = head
"""


# Dummy Pointers

"""
Dummy pointers

As mentioned earlier, we usually want to keep a reference to the head to ensure we can always access any element.
Sometimes, it's better to traverse using a "dummy" pointer and to keep head at the head.

"""

def get_sum(head):
    ans = 0
    dummy = head
    while dummy:
        ans += dummy.val
        dummy = dummy.next

    # same as before, but we still have a pointer at the head
    return ans