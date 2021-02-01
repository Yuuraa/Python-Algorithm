from collections import defaultdict

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def vertical_traversal(root):
    curr = root
    answer, x_dicts = [], defaultdict(list)

    def traverse_tree(root, x, y):
        if root:
            x_dicts[x].append((root, y))
        if root.left:
            traverse_tree(root.left, x - 1, y - 1)
        if root.right:
            traverse_tree(root.right, x + 1, y - 1)

    traverse_tree(root, 0, 0)
    x_vals = sorted(list(x_dicts.keys()))

    for x_val in x_vals:
        answer.append([x[0] for x in sorted(x_dicts[x_val], key=lambda x: (-x[1], x[0]))])

    return answer


# TODO
# def make_tree(val_list):
#     n = len(val_list)
#     for i, val in enumerate(node_list):
#         new_node = ListNode(val)
#         if 2*i + 2 < n:



