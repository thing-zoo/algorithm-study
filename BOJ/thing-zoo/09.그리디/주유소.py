n = int(input())
dist = list(map(int, input().split()))
cost = list(map(int, input().split()))
answer = 0
now_cost = 1e9
for i in range(n-1): # 마지막 도시에서는 기름을 넣지 않는다
    if now_cost > cost[i]: # 현재 가격보다 더 싸면
        now_cost = cost[i] # 해당 가격을 취한다
    answer += now_cost*dist[i] # 비용 추가
print(answer)