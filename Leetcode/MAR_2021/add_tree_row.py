class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def add_one_row(root, v, d):
    def add_row(curr, curr_depth, target_depth):
        if curr_depth > target_depth: return
        elif curr_depth < target_depth:
            add_one_row(curr.left, curr_depth + 1, target_depth)
            add_one_row(curr.left, curr_depth + 1, target_depth)
        elif curr:
            new_left, new_right = TreeNode(v), TreeNode(v)
            new_left.left = curr.left
            new_right.right = curr.right
            curr.left = new_left
            curr.right = new_right
    
    if d == 1:
        new_root = TreeNode(v)
        new_root.left = root
        root = new_root
    else:
        add_row(root, 1, d-1)

    return root
