class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sorted_arr_to_bst(nums):
    def append_subs(sub_nums):
        if not sub_nums: return
        mid = len(sub_nums)//2
        rootNode = TreeNode(sub_nums[mid])
        rootNode.left = append_subs(sub_nums[:mid])
        rootNode.right = append_subs(sub_nums[mid+1:])
        return rootNode
    return append_subs(nums)