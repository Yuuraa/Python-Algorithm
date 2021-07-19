# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def lowestCommonAncestor(root, p, q):
    if p.val > q.val: p, q = q, p
    
    while True:
        if p.val <= root.val and q.val >= root.val: return root
        if p.val < root.val: # 둘 다 root보다 왼쪽에 있을 때
            root = root.left
        else: # 둘 다 root 보다 오른 쪽에 있을 때
            root = root.right
    
    return None