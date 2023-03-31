import sys
input = sys.stdin.readline
sys.setrecursionlimit(3000)

def check(i, j):
    global field
    global n,m
    if i >= n or i < 0 or j >= m or j< 0:
        return False
    if field[i][j] == 1:
        field[i][j] = 0
        check(i+1, j)
        check(i, j+1)
        check(i-1, j)
        check(i, j-1)
        return True
    else:
        return False

total = int(input())

for t in range(total):
    m, n, k = map(int, input().split())
    field = [[0] * m for _ in range(n)]
    res = 0
    for i in range(k):
        a, b = map(int, input().split())
        field[b][a] = 1

    for i in range(n): 
        for j in range(m): 
            if check(i, j) == True:
                res += 1

    print(res)