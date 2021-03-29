class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    

def filp_match_voyage(root, voyage):
    traverse_list = [root]
    idx, ans = 0, []
    while traverse_list:
        curr = traverse_list.pop()
        if curr.val != voyage[idx]:
            return [-1]
        if idx == len(voyage) - 1: break
        left, right = curr.left, curr.right
        if left and right:
            if left.val != voyage[idx + 1]:
                left, right = right, left
                ans.append(curr.val)
            traverse_list.append(right)
            traverse_list.append(left)
        elif left:
            traverse_list.append(left)
        elif right:
            traverse_list.append(right)
        idx += 1

    return ans