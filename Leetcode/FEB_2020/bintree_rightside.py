from collections import defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def right_side_view(root):
    height_vals = defaultdict(list)
    answer = []

    def add_vals(curr, height):
        if not curr: return
        height_vals[height].append(curr)
        # 왼쪽의 값을 먼저 추가해 가장 오른쪽의 값이 리스트의 맨 끝에 저장되게 한다
        add_vals(curr.left, height + 1)
        add_vals(curr.right, height + 1)

    add_vals(root, 0)
    for h in sorted(list(height_vals.keys())):
        answer.append(height_vals[h][-1])

    return answer
