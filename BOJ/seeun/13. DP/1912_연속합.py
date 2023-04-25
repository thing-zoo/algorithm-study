import sys
input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().rstrip().split()))

# 원래 있던 배열 그대로 사용
# 지금 수 vs 이전 수 + 지금 수 중에 더 큰 값으로 대체
for i in range(1, n):
    # 어디선가부터 i번째 까지의 연속된 최대합
    nums[i] = max(nums[i], nums[i-1] + nums[i])
print(max(nums))