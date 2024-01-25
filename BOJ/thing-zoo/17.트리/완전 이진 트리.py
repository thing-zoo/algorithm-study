class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inorder(node):
    global idx
    if node.left:
        inorder(node.left)
    node.data = order[idx]
    idx += 1
    if node.right:
        inorder(node.right)
k = int(input())
order = list(map(int, input().split()))
tree = {}
idx = pow(2, k)-1
for i in range(k-1, -1, -1):
    for j in range(pow(2, i)):
        tree[idx] = Node(0)
        if idx*2 in tree:
            tree[idx].left = tree[idx*2]
        if idx*2+1 in tree:
            tree[idx].right = tree[idx*2+1]
        idx -= 1
inorder(tree[1])
for i in range(k):
    for j in range(pow(2, i)):
        print(tree[pow(2,i)+j].data, end=' ')
    print()