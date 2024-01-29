class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
def preorder(node):
    print(node.data, end='')
    if node.left:
        preorder(node.left)
    if node.right:
        preorder(node.right)
def inorder(node):
    if node.left:
        inorder(node.left)
    print(node.data, end='')
    if node.right:
        inorder(node.right)
def postorder(node):
    if node.left:
        postorder(node.left)
    if node.right:
        postorder(node.right)
    print(node.data, end='')

n = int(input())
tree = {}
for _ in range(n):
    data, left, right = input().split()
    if data not in tree:
        tree[data] = Node(data)
    if left != '.':
        if left not in tree:
            tree[left] = Node(left)
        tree[data].left = tree[left]
    if right != '.':
        if right not in tree:
            tree[right] = Node(right)
        tree[data].right = tree[right]
preorder(tree['A'])
print()
inorder(tree['A'])
print()
postorder(tree['A'])