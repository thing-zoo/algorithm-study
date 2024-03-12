import sys
input = sys.stdin.readline

n = int(input())
honey = list(map(int, input().rstrip().split()))

# 각 위치별 누적합 구하기
total = [0]*n
total[0] = honey[0]
for i in range(1, n):
    total[i] += total[i-1] + honey[i]

# 최대 꿀의 양 구하기
answer = 0
# 벌(0)-벌-벌통(n-1)
for i in range(1, n-1): # 나머지 벌 위치 고르기
    answer = max(answer, (total[-1]-honey[0]-honey[i])+(total[-1]-total[i]))
# 벌통(0)-벌-벌(n-1)
for i in range(1, n-1): # 나머지 벌 위치 고르기
    answer = max(answer, (total[-1]-honey[-1]-honey[i])+total[i-1])
# 벌(0)-벌통-벌(n-1)
for i in range(1, n-1): # 벌통 위치 고르기
    answer = max(answer, (total[i]-honey[0])+(total[-1]-total[i-1]-honey[-1]))
print(answer)