n, m, l = map(int, input().split())
nums = list(map(int, input().split()))
nums.append(l)
nums.sort()
s = 1
e = l-1
ans = 0

# 휴게소 없는 구간의 최댓값을 최소로
while s<=e:
    mid = (s+e)//2
    # 최대 구간 구하기
    cnt = (nums[0]-0-1)//mid
    for i in range(1, len(nums)):
        if nums[i]-nums[i-1] > mid:
            cnt += (nums[i] - nums[i-1]-1)//mid # 두 휴게소 사이의 거리가 mid보다 큰 곳에 휴게소 *개 설치
    
    if cnt > m: # 휴게소 설치한 개수가 m보다 많으면
        s = mid +1
    else:
        ans  = mid
        e = mid -1
print(ans)