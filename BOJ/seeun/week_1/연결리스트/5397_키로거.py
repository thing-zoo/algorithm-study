import sys
n = int(input())

for i in range(n):
    pw = list(sys.stdin.readline().strip())
    left = []
    right = []
    for j in pw:
        # print(j)
        if j == "<":
            if len(left)>0:
                tmp = left.pop()
                right = [tmp]+right
        elif j == ">":
            if len(right)>0:
                left = left + [right[0]]
                right = right[1:]
        elif j == "-":
            if len(left)>0:
                left.pop()
        else:
            left.append(j)
        print(left, right)
        
    print(*left, *right, sep="")