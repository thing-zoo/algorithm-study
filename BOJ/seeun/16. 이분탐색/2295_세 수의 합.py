n = int(input())
nums = [int(input()) for _ in range(n)]

nums.sort()
sumList = []
ans = 0

# x+y+z=k => x+y=k-z를 이용

# x+y를 저장하는 sumList
for i in range(n):
    for j in range(i, n):
        sumList.append(nums[i]+nums[j])

sumList.sort()
# k-z가 sumList에 있는지 확인
for i in range(n):
    for j in range(i, n):
        tmp = nums[j]-nums[i] # k-z
        s = 0
        e = len(sumList)-1
        while s<=e:
            m = (s+e)//2
            if tmp == sumList[m]:
                ans = max(nums[j], ans) # 가장 큰 수 저장
                break
            elif tmp>sumList[m]:
                s = m+1
            else:
                e = m-1

print(ans)