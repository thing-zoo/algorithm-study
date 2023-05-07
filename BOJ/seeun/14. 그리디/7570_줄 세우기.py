import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().rstrip().split()))

d = [0]*(n+1)
# 가장 긴 연속된 수열
for i in range(n):
    idx = nums[i] #학생번호: idx
    d[idx] = d[idx-1]+1

# 최소로 움직이는 방법: 연속된 수열은 그대로 두고 나머지만 이동
print(n-max(d))