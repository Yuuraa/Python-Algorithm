class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_k_lists(lists):
    new_head = ListNode()
    new_curr = new_head
    total_vals = []
    for curr_node in lists:
        while curr_node:
            total_vals.append(curr_node.val)
            curr_node = curr_node.next
    total_vals.sort()
    for val in total_vals:
        new_curr.next = ListNode(val)
        new_curr = new_curr.next
    return new_head.next

