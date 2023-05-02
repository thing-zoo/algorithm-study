n = int(input())
data = [int(input()) for _ in range(n)]
answer = 0 # 감소시킨 횟수
level_point = data[-1]
for i in range(n-2, -1, -1):
    level_point = min(level_point - 1, data[i]) # 레벨 i의 점수
    answer += data[i] - level_point
print(answer)
