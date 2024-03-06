import sys
input = sys.stdin.readline # 입력시 시간초과 발생으로 추가
n = int(input())
cost = [int(input()) for _ in range(n)]
cost.sort(reverse=True) # 고가순으로 정렬 후
answer = 0
for i in range(0, n, 3): # 세개씩 묶어
    if i < n: answer += cost[i]
    if i+1 < n: answer += cost[i+1]
    # 세번째 물건값만 제외
print(answer)