def star(n, a, b):
    if n == 3:
        for i in range(3):
            for j in range(5):
                graph[a+i][b+j] = pattern[i][j]
        return
    
    star(n//2, a, b+(2*n//4))
    star(n//2, a+(n//2), b)
    star(n//2, a+(n//2), b+(2*n//2))
n = int(input())
graph = [[" "]*(2*n-1) for _ in range(n)]
pattern = [ "  *  ",
            " * * ",
            "*****"]
star(n, 0, 0)
for g in graph:
    print("".join(g))