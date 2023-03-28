def star(n, a, b):
    if n == 3:
        for i in range(a, a+n):
            for j in range(b, b+n):
                if i == a+n//2 and j == b+n//2:
                    continue
                graph[i][j] = "*"
        return
    
    next = n//3
    for i in range(3):
            for j in range(3):
                if i == j == 1:
                    continue
                star(next, a+(i*next), b+(j*next))
n = int(input())
graph = [[" "]*n for _ in range(n)]
star(n, 0, 0)
for i in range(n):
    print(*graph[i], sep="")