n = int(input())
nums = list(map(int, input().split()))

ans = sum(nums[:3])
liquid = []
nums.sort()
if nums[0]>0: # 모두 양수일때 처음 세개 뽑기
    liquid = nums[:3]
elif nums[-1]<0: # 모두 음수일때 마지막 세개 뽑기
    liquid = nums[-3:]
else: # 섞여있을 때
    for i in range(n-2):
        s = i+1
        e = n-1
        while s<e:
            if s!=i and e != i and sum([nums[s], nums[e], nums[i]])== 0: # 합이 0이면 바로 끝
                ans = 0
                liquid = [nums[s], nums[e], nums[i]]
                break
            elif abs(sum([nums[s], nums[e], nums[i]])) < abs(ans):
                ans = abs(sum([nums[s], nums[e], nums[i]]))
                liquid = [nums[s], nums[e], nums[i]]
            
            if sum([nums[s], nums[e], nums[i]]) < 0:
                s += 1
            elif sum([nums[s], nums[e], nums[i]]) > 0:
                e -= 1
        if ans == 0:
            break
liquid.sort()
print(*liquid)