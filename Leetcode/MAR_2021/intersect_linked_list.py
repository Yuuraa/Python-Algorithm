class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def get_intersection_node(headA, headB):
    currA, currB = headA, headB
    lenA, lenB = 0, 0
    
    while currA:
        lenA += 1
        currA = currA.next
    while currB:
        lenB += 1
        currB = currB.next

    currA, currB = headA, headB
    if lenA > lenB:
        for _ in range(lenA - lenB):
            currA = currA.next
    else:
        for _ in range(lenB - lenA):
            currB = currB.next
    
    while currA and currB:
        if currA == currB:
            return currA
        else:
            currA = currA.next
            currB = currB.next
    
    return None


def get_intersection_node_other(headA, headB):
    p, q = headA, headB
    while p != q:
        p = p.next if p else headB
        q = q.next if q else headA
    return p