from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def average_of_levels(root):
    node_per_height = defaultdict(list)

    curr, height = root, 0
    node_per_height[height].append(curr.val)

    def traverse_tree(curr, height):
        if curr:
            node_per_height[height].append(curr.val)
            traverse_tree(curr.left, height + 1)
            traverse_tree(curr.right, height + 1)

    traverse_tree(curr.left, height + 1)
    traverse_tree(curr.right, height + 1)

    return [sum(node_per_height[h])/len(node_per_height[h]) for h in sorted(list(node_per_height.keys()))]


def average_of_levels_bfs(root):
    if not root: return []

    result = []
    curr_height = [root]
    next_height = []

    while curr_height:
        height_nodes = []
        next_height = []

        for node in curr_height:
            height_nodes.append(node.val)
            if node.left:
                next_height.append(node.left)
            if node.right:
                next_height.append(node.right)
        
        result.append(sum(height_nodes)/len(height_nodes))
        curr_height = next_height
    return result
