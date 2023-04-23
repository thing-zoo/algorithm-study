import sys
input = sys.stdin.readline

n = int(input())
count = [0]*(10000+1)

# 값 카운팅
for _ in range(n):
    x = int(input().rstrip())
    count[x] += 1

# 결과
for i in range(1, len(count)):
    for _ in range(count[i]):
        sys.stdout.write(str(i)+'\n')