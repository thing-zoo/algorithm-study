import sys
input = sys.stdin.readline
bag, n = map(int, input().split())
jew = [list(map(int, input().split())) for _ in range(n)]
jew.sort(key=lambda x:(-x[1]))

ans = 0 # 가격
weight = 0 # 담은 무게

for i in range(n):
  if jew[i][0] < bag-weight: # 해당 보석을 다 담을 수 있을만큼 자리가 있으면
    weight += jew[i][0] # 다 담기
    ans += jew[i][0]*jew[i][1] # 가격 더해주기
  else: # 해당 보석을 넣을 수 있을 만큼만 넣음
    ans += jew[i][1] * (bag-weight) # 남은 용량 만큼만 넣음
    weight += bag-weight
  if weight == bag:
    break

print(ans)