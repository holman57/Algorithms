# Given the head of a linked list, your task is to check
#   whether the linked list is a palindrome or not. Return
#   TRUE if the linked list is a palindrome; otherwise, return FALSE.

class LinkedListNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def palindrome(head):
    slow, fast = head, head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next

    prev = None
    while slow:
        next_node, slow.next = slow.next, prev
        prev, slow = slow, next_node

    while prev:
        if head.data != prev.data:
            return False
        head, prev = head.next, prev.next

    return True


def test_palindrome():
    # Test case 1: Empty list
    assert palindrome(None) == True

    # Test case 2: Single element list
    head = LinkedListNode(1)
    assert palindrome(head) == True

    # Test case 3: Palindrome list with even length
    head = LinkedListNode(1, LinkedListNode(2, LinkedListNode(2, LinkedListNode(1))))
    assert palindrome(head) == True

    # Test case 4: Palindrome list with odd length
    head = LinkedListNode(1, LinkedListNode(2, LinkedListNode(3, LinkedListNode(2, LinkedListNode(1)))))
    assert palindrome(head) == True

    # Test case 5: Non-palindrome list with even length
    head = LinkedListNode(1, LinkedListNode(2, LinkedListNode(3, LinkedListNode(4))))
    assert palindrome(head) == False

    # Test case 6: Non-palindrome list with odd length
    head = LinkedListNode(1, LinkedListNode(2, LinkedListNode(3, LinkedListNode(4, LinkedListNode(5)))))
    assert palindrome(head) == False


test_palindrome()
print("All test cases passed!")
