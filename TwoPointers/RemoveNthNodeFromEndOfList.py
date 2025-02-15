# Given the head of a singly linked list, remove
#   the nth node from the end of the list and return its head.

# Definition for a Linked List node

class LinkedListNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def remove_nth_last_node(head, n):
    fast, slow = head, head
    for _ in range(n):
        if fast is None:
            # n is greater than the length of the list
            return head
        fast = fast.next

    # n is equal to the length of the list
    if fast is None:
        return head.next

    while fast.next:
        fast, slow = fast.next, slow.next

    slow.next = slow.next.next
    return head


def test_remove_nth_last_node():
    # Test case 1: Removing the 2nd last node from a list of 5 nodes
    head = LinkedListNode(1, LinkedListNode(2, LinkedListNode(3, LinkedListNode(4, LinkedListNode(5)))))
    expected = LinkedListNode(1, LinkedListNode(2, LinkedListNode(3, LinkedListNode(5))))
    actual = remove_nth_last_node(head, 2)
    assert compare_linked_lists(actual, expected)

    # Test case 2: Removing the last node from a list of 5 nodes
    head = LinkedListNode(1, LinkedListNode(2, LinkedListNode(3, LinkedListNode(4, LinkedListNode(5)))))
    expected = LinkedListNode(1, LinkedListNode(2, LinkedListNode(3, LinkedListNode(4))))
    actual = remove_nth_last_node(head, 1)
    assert compare_linked_lists(actual, expected)

    # Test case 3: Removing the 5th last node (head) from a list of 5 nodes
    head = LinkedListNode(1, LinkedListNode(2, LinkedListNode(3, LinkedListNode(4, LinkedListNode(5)))))
    expected = LinkedListNode(2, LinkedListNode(3, LinkedListNode(4, LinkedListNode(5))))
    actual = remove_nth_last_node(head, 5)
    assert compare_linked_lists(actual, expected)

    # Test case 4: Removing from an empty list
    head = None
    expected = None
    actual = remove_nth_last_node(head, 1)
    assert compare_linked_lists(actual, expected)

    # Test case 5: Removing a node from a list of 1 node
    head = LinkedListNode(1)
    expected = None
    actual = remove_nth_last_node(head, 1)
    assert compare_linked_lists(actual, expected)

    # Test case 6: n is greater than the length of the list
    head = LinkedListNode(1, LinkedListNode(2, LinkedListNode(3)))
    expected = LinkedListNode(1, LinkedListNode(2, LinkedListNode(3)))
    actual = remove_nth_last_node(head, 4)
    assert compare_linked_lists(actual, expected)


def compare_linked_lists(head1, head2):
    while head1 and head2:
        if head1.data != head2.data:
            return False
        head1 = head1.next
        head2 = head2.next
    return head1 is None and head2 is None


test_remove_nth_last_node()
print("All test cases passed!")
