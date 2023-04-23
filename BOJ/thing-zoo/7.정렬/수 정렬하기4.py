import sys
input = sys.stdin.readline

n = int(input())
count = [ [0]*(1000000+1) for _ in range(2) ]

# 값 카운팅
for _ in range(n):
    x = int(input().rstrip())
    if x < 0:
        count[1][-x] += 1
    else:
        count[0][x] += 1

# 결과
for i in range(1000000, -1, -1):
    for _ in range(count[0][i]):
        sys.stdout.write(str(i)+'\n')

for i in range(1, 1000001):
    for _ in range(count[1][i]):
        sys.stdout.write(str(-i)+'\n')