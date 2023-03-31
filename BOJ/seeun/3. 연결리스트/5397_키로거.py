import sys
n = int(input())

for i in range(n):
    pw = list(sys.stdin.readline().strip())
    origin = []
    temp = []
    for j in pw:
        if j == "<":
            if origin:
                temp.append(origin.pop())
        elif j == ">":
            if temp:
                origin.append(temp.pop())
        elif j == "-":
            if origin:
                origin.pop()
        else:
            origin.append(j)
        
    while temp:
        origin.append(temp.pop())

    print(*origin, sep="")