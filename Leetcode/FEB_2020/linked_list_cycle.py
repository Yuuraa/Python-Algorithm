class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle(head):
    curr, i = head, 0
    while curr and i < int(1e4) + 1:
        i += 1
        curr = curr.next
        
    return curr != None


def hasCycle_proper(head):
    slow = fast = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if slow == fast: return True

    return False