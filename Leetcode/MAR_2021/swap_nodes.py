class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        fake_head = ListNode(next=head)
        curr = fake_head
        nodes = []
        while curr:
            nodes.append(curr)
            curr = curr.next
        n = len(nodes) - 1
        
        if n == 2*k - 2:
            nodes[-k].next = nodes[k].next
            nodes[-k-1].next = nodes[k]
            nodes[k].next = nodes[-k]
        elif n == 2*k:
            nodes[k].next = nodes[-k].next
            nodes[k-1].next = nodes[-k]
            nodes[-k].next = nodes[k]
        else:
            nodes[k].next, nodes[-k].next = nodes[-k].next, nodes[k].next
            nodes[k-1].next, nodes[-k-1].next = nodes[-k], nodes[k]
            
        return fake_head.next

class SolutionOther:
    def swapNodes(self, head, k):
        n = 0
        beg = head
        while beg:
            if n == k-1: l = beg
            beg = beg.next
            n += 1
        
        r = head
        for m in range(n-k):
            r = r.next
                
        l.val, r.val = r.val, l.val
        return head