import sys
input = sys.stdin.readline
n, k = map(int, input().split())
scores = [0] + list(map(int, input().split()))
# 누적합 구하기
for i in range(1, n+1):
  scores[i] += scores[i-1]

# 평균 구하기
for _ in range(k):
  a, b = map(int, input().split())
  avg = scores[b] - scores[a-1]
  avg = round(avg/(b-a+1), 2)
  print(format(avg, ".2f")) # 소수점 둘째자리까지 출력