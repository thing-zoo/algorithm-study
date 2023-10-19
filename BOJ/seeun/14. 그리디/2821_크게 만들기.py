import sys
input = sys.stdin.readline
N, K = map(int, input().rstrip().split())
nums = list(input().rstrip())
nums = list(map(int, nums))
stack = []
cnt = K
for i in range(N): # 첫번째 수부터
        while stack and stack[-1] < nums[i] and cnt > 0: # 이전 숫자보다 큰 숫자만 남아있을 수 있도록
            stack.pop()
            cnt -= 1
        stack.append(nums[i])
print("".join(map(str, stack[:N-K]))) # 최대 길이만큼만 출력