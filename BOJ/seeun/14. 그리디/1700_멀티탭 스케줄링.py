n, k = map(int, input().split())
nums = list(map(int, input().split()))
tap = []
mincount = 0
for i in range(k):
    if nums[i] in tap:
        continue
    else:
        if len(tap) < n:
            tap.append(nums[i])
        else: # 멀티탭이 꽉찼으면
            # pull = 99999 # 뽑을 번호
            # cnt = 99999
            # for j in tap: # 멀티탭에 꼽혀있는 것 중에서 앞으로 제일 적게 쓰일 애를 뽑음
            #     if cnt >= nums[i+1:].count(j):
            #         cnt = nums[i+1:].count(j)
            #         pull = j
            # tap[tap.index(pull)] = nums[i]
            # mincount += 1
            far = -1
            farindex = -1
            for j in range(n): # 멀티탭에 있는 것 중에 앞으로 가장 나중에 쓰일 애를 뽑음
                tmp = 0
                for p in range(i+1, k, 1): # 얼마나 떨어져있는지 세아리기
                    if nums[p] == tap[j]:
                        break
                    else: # 거리 +1
                        tmp += 1
                if far<tmp:
                    far = tmp # 얼마나 떨어져있는지 최대값
                    farindex = j # 멀티탭에서 그 기기가 몇번째인지
            tap[farindex] = nums[i]
            mincount += 1
print(mincount)