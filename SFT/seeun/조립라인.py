import sys
input = sys.stdin.readline
n = int(input())
info = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
  info[i][0] += min(info[i-1][0], info[i-1][1] + info[i-1][3]) # 0에서 그대로 오기 vs 1->0으로 오기
  info[i][1] += min(info[i-1][1], info[i-1][0] + info[i-1][2]) # 1에서 그대로 오기 vs 0->1로 오기

print(min(info[-1])) # 둘 중에 더 빨리 끝나는 작업 라인 시간 출력