class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def inorder(node):
    if node:
        inorder(node.left)
        print(node.data, end=' ')
        inorder(node.right)

def preorder(node):
    if node:
        print(node.data, end=' ')
        preorder(node.left)
        preorder(node.right)

def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.data, end=' ')   
        
from collections import deque

def level_order(root):
    result = []
    
    if not root:
        return
    queue = deque([root])
    while queue:
        ans = []
        node = queue.popleft()
        ans.append(node.data)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
        result.append(ans)
    return result
        


        
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(5)


print(level_order(root))
# inorder(root)
# print()
# preorder(root)
# print()
# postorder(root)
