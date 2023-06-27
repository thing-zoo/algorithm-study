n = int(input())
tree = {}
for _ in range(n):
    nodes = input().split()
    tree[nodes[0]] = nodes[1:]

def preorder(start):
    if start == '.':
        return
    print(start, end="")
    for n in tree[start]:
        preorder(n)

def inorder(start):
    if start == '.':
        return
    inorder(tree[start][0])
    print(start, end="")
    inorder(tree[start][1])

def postorder(start):
    if start == '.':
        return
    postorder(tree[start][0])
    postorder(tree[start][1])
    print(start, end="")
preorder('A')
print()
inorder('A')
print()
postorder('A')