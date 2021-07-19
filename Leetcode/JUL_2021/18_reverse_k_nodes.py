# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseGroup(self, prev, curr, k):
    s = curr
    i = 0
    for i in range(k-1):
        curr = curr.next
        if not curr: return

    if not curr: return
    e = curr
    sn = s.next
        
    while s != e:
        s.next = e.next
        e.next = s
        s = sn
        sn = s.next
        
    prev.next = s


def reverseKGroup(head, k):
    fake_head = ListNode(-1, head)
    prev, curr = fake_head, head
    if k == 1: return head
        
    while curr:
        reverseGroup(prev, curr, k)
        prev = curr
        curr = curr.next
    return fake_head.next
