class Node:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class BinarySearchTree:
    def __init__(self, head):
        self.head = head

    def insert(self, val):
        self.current_node = self.head
        while self.current_node:
            if val < self.current_node.val:
                if self.current_node.left:
                    self.current_node = self.current_node.left
                else:
                    self.current_node.left = Node(val)
                    break
            else:
                if self.current_node.right:
                    self.current_node = self.current_node.right
                else:
                    self.current_node.right = Node(val)
                    break
    
    def search(self, val):
        self.current_node = self.head
        while self.current_node:
            if val == self.current_node:
                return True
            elif val < self.current_node.val:
                self.current_node = self.current_node.left
            else:
                self.current_node = self.current_node.right
        return False
    
    # TODO: delete 구현
