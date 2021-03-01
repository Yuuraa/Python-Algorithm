class Node:
    def __init__(self, x:int, next:'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


def copy_random_list(head: 'Node') -> 'Node':
    original_nodes, new_nodes = [], []
    if not head: return head

    def refer_or_make(old_node):
        if old_node in original_nodes:
            return new_nodes[original_nodes.index(old_node)]
        else:
            original_nodes.append(old_node)
            new_node = Node(old_node.val)
            new_nodes.append(new_node)
            return new_node
    
    curr = head
    while curr:
        curr_new = refer_or_make(curr)
        if curr.next:
            new_next = refer_or_make(curr.next)
            curr_new.next = new_next
        if curr.random:
            new_random = refer_or_make(curr.random)
            curr_new.random = new_random

        curr = curr.next

    return new_nodes[0]