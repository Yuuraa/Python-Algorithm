def prune_tree(root):
    def check_prune(curr):
        if not curr: return False
        if not check_prune(curr.left):
            curr.left = None
        if not check_prune(curr.right):
            curr.right = None
        if curr.val == 1: return True
        else:
            return curr.left | curr.right

    if not check_prune(root):
        root = None
    return root