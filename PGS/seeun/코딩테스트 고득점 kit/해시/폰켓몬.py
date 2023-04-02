nums = [3,3,3,2,2,4]
def solution(nums):
    answer = 0
    mon_num = dict()

    for i in nums:
        if i in mon_num:
            mon_num[i] += 1
        else:
            mon_num[i] = 1
    print(mon_num)
    limit = len(nums)//2
    if len(mon_num.keys()) < limit:
        answer = len(mon_num.keys())
    else:
        answer = limit
    return answer

print(solution(nums))