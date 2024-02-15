n = int(input())
nums = list(map(int, input().split()))
nums.sort()
minnum = float('inf')
minlist = []
s, e = 0, n-1
while s < e:
    # 0에 가장 가까운 값 찾기
    if abs(minnum) > abs(nums[s] + nums[e]):
        minnum = nums[s] + nums[e]
        minlist = [nums[s], nums[e]]

    # 0에 더 가깝게 하기 위해 인덱스 조정
    if nums[s] + nums[e] < 0:
        s += 1
    elif nums[s] + nums[e] > 0:
        e -= 1
    else:
        break

print(" ".join(map(str, minlist)))