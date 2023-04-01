import sys
left = list(input())
right = []
m = int(input())

for _ in range(m):
    order = sys.stdin.readline().split()
    
    if order[0] == "L":
        if left:
            right.append(left.pop())
    elif order[0] == "D":
        if right:
            left.append(right.pop())
    elif order[0] == "B":
        if left:
            left.pop()
    else: # P
        left.append(order[1])

print("".join(left)+"".join(reversed(right)))