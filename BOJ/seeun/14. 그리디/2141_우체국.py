import sys
input = sys.stdin.readline
n = int(input())
nums = []
total = 0
for _ in range(n):
    t, a = map(int, input().split())
    total += a # 전체 인구수 저장
    nums.append([t, a])
nums.sort()

cnt = 0
for i in range(n):
    cnt += nums[i][1] # 왼쪽부터 돌면서
    if cnt > total/2: # 누적 인구 수가 전체 인구수 절반을 넘어가는 시점의
        print(nums[i][0]) # 마을 위치 출력
        break
