n = int(input())
nums = list(map(int, input().split()))
nums.sort()

s = 0
e = n-1
ans = abs(nums[s] + nums[e]) # 용액 두개의 최소 절댓값 저장
liquid = [nums[s], nums[e]] # 최소 절댓값을 만드는 용액 두 가지 저장
while s<e:
    if abs(nums[s] + nums[e]) == 0: # 두가지 용액이 0이 된다면 정답이므로 출력
        ans = 0
        liquid = [nums[s], nums[e]]
        break
    elif abs(nums[s] + nums[e]) < ans : # 현재 용액이 최솟값보다 작다면 최솟값 갱신
        ans = abs(nums[s] + nums[e] )
        liquid  = [nums[s], nums[e]]

    if nums[s] + nums[e]<0: # 두 용액의 합이 음수이면 s를 오른쪽으로 한칸 옮김
        s += 1
    elif nums[s] + nums[e] >0: # 양수이면 e를 왼쪽으로 한칸 옮김
        e -= 1

liquid.sort()
print(*liquid)