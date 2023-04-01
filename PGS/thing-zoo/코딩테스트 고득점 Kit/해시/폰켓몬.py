def solution1(nums): #나의 스파게티 코드..
    answer = []
    n = len(nums)
    d = {}
    for i in nums:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    i = 0
    while i < n//2:
        for k, v in d.items():
            if i == n//2: break
            if not v: continue
            d[k] = v-1
            i += 1
            if k not in answer:
                answer.append(k)
    return len(answer)

def solution2(nums): # 혁명적인 다른분 답...
    return min(len(nums)/2, len(set(nums)))

nums = 	[3, 1, 2, 3]
print(solution1(nums))