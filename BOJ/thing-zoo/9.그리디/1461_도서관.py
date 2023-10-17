n, m = map(int, input().split())
pos = list(map(int, input().split()))
pos.sort(key=lambda x: abs(x), reverse=True) # 절댓값 기준 내림차순 정렬

# 음수 양수 나누기
plus = []
minus = []
for i in range(n):
    if pos[i] > 0: plus.append(pos[i])
    else: minus.append(abs(pos[i]))

# 걸음수 구하기(절댓값 최대값은 편도로 가는게 최소 걸음수)
answer = 0
for i in range(0, len(plus), m):
    if plus[i] == pos[0]: answer += plus[i]
    else: answer += plus[i]*2
for i in range(0, len(minus), m):
    if minus[i] == abs(pos[0]): answer += minus[i]
    else: answer += minus[i]*2
print(answer)