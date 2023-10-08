import sys
input = sys.stdin.readline
n = int(input())
info = []
for _ in range(n):
    info.append(list(map(int, input().split())))

rank = [1] * n # 모두 1등으로 초기화
for i in range(n):
    for j in range(n):
        if info[i][0] < info[j][0] and info[i][1] < info[j][1]: # 덩치 큰 사람 만나면 등수 +1
            rank[i] += 1

print(*rank)