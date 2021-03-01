class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def trim_bst(root, low, high):
    def dfs(curr):
        if not curr:
            return None
        if low <= curr.val <= high:
            curr.left = dfs(curr.left)
            curr.right = dfs(curr.right)
            return curr
        else:
            if curr.left:
                valid_left = dfs(curr.left)
                if valid_left:
                    return valid_left
            if curr.right:
                valid_right = dfs(curr.right)
                if valid_right:
                    return valid_right
            return None
            
    root = dfs(root)
    return root


def trim_bst_other(root, high, low):
    def dfs(node):
        if not node: return node
        if node.val > high:
            return dfs(node.left)
        elif node.val < low:
            return dfs(node.right)
        else:
            node.left = dfs(node.left)
            node.right = dfs(node.right)
            return node

    return dfs(root)