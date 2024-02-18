def get_cost(a):
    if a[0] == a[1] == a[2]:
        cost = 0
    else:
        mid = sorted(a)[1]
        cost = sum([abs(x-mid) for x in a])
    return cost
    
h = [list(map(int, input().split())) for _ in range(3)]
answer = 1e9 # 농사 지을 땅을 만드는데 필요한 최소 비용

# 가로줄 확인
for i in range(3):
    answer = min(answer, get_cost(h[i]))
# 세로줄 확인
for i in range(3):
    temp = [h[j][i] for j in range(3)]
    answer = min(answer, get_cost(temp))
print(answer)