n, m = map(int, input().split())

def rotate(before):
    after = [[0]*n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            after[j][n-i-1] = before[i][j]
    return after

row = [list(input()) for _ in range(n)]
col = rotate(row)

rcnt, ccnt = 0, 0
for i in range(n):
    if row[i].count('X') == 0:
        rcnt += 1

for i in range(m):
    if col[i].count('X') == 0:
        ccnt += 1
    
print(max(rcnt, ccnt))