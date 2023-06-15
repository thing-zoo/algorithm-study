import sys
input = sys.stdin.readline
n, m = map(int, input().rstrip().split())
nums = [[] for _ in range(n+1)]
nums[0] = [0]*(n+1) # 0번째행 0으로 초기화

for i in range(1, n+1):
    nums[i].append(0) # 0번째열 0으로 초기화
    nums[i].extend(list(map(int, input().rstrip().split())))

# nums[i][j] = 0, 0부터 i, j까지 직사각형 모양의 누적합
for i in range(1, n+1):
    for j in range(1, n+1):
        nums[i][j] = nums[i][j] + nums[i][j-1] + nums[i-1][j] - nums[i-1][j-1]

# nums[bi][bj]에서 포함되지 않는 직사각형들을 계산을 통해 빼주기
for _ in range(m):
    ai, aj, bi, bj = map(int, input().rstrip().split())
    ans = nums[bi][bj] - nums[ai-1][bj] - nums[bi][aj-1] + nums[ai-1][aj-1]
    print(ans)