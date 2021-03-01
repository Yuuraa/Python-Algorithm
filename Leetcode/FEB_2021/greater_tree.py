class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def convert_bst(slef, root:TreeNode) -> TreeNode:
    def inorder_traverse(curr, total_val):
        if curr.right:
            total_val = inorder_traverse(curr.right, total_val)
        curr.val = curr.val + total_val
        total_val = curr.val
        if curr.left:
            total_val = inorder_traverse(curr.left, total_val)

        return total_val

    if not root: return root
    inorder_traverse(root, 0)

    return root