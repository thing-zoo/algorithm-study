import copy
def rotate(n, arr): # 시계방향
    res = copy.deepcopy(arr)
    for i in range(n):
        # 주대각선 -> 가운데열
        res[i][(n+1)//2-1] = arr[i][i]
        # 가운데열 -> 부대각선
        res[i][n-1-i] = arr[i][(n+1)//2-1]
        # 부대각선 -> 가운데행 
        res[(n+1)//2-1][n-1-i] = arr[i][n-1-i]
        # 가운데행 -> 주대각선
        res[i][i] = arr[(n+1)//2-1][i]
    return res

def rotate2(n, arr): # 반시계방향
    res = copy.deepcopy(arr)
    for i in range(n):
        # 주대각선 -> 가운데행
        res[(n+1)//2-1][i] = arr[i][i]
        # 가운데열 -> 주대각선
        res[i][i] = arr[i][(n+1)//2-1]
        # 부대각선 -> 가운데열
        res[i][(n+1)//2-1] = arr[i][n-1-i]
        # 가운데행 -> 부대각선
        res[n-1-i][i] = arr[(n+1)//2-1][i]
    return res

t = int(input())
for _ in range(t):
    n, d = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    
    m = abs(d)//45
    for _ in range(m):
        if d > 0:
            arr = rotate(n, arr)
        else:
            arr = rotate2(n, arr)
    
    for i in range(n):
        for j in range(n):
            print(arr[i][j], end=' ')
        print()