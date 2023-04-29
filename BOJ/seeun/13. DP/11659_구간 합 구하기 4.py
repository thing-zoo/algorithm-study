import sys
input = sys.stdin.readline
n, m = map(int, input().rstrip().split())
nums = list(map(int, input().rstrip().split()))
num_sum = [0]*(n+1)
# 구간 별 합 구하기
for i in range(1, n+1):
    num_sum[i] = nums[i-1]+num_sum[i-1]

# 끝점 - 시작점으로 계산
for _ in range(m):
    a, b = map(int, input().rstrip().split())
    print(num_sum[b]-num_sum[a-1])