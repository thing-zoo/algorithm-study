from collections import defaultdict


r, c, k = map(int, input().split())
nums = []
for _ in range(3):
    nums.append(list(map(int, input().split())))

time = 0
flag = False
while time<=100:
    if len(nums)>=r and len(nums[0])>=c and nums[r-1][c-1] == k:
        flag = True
        break

    # R
    if len(nums)>=len(nums[0]):
        # print("R")
        for i in range(len(nums)): #행 별로 정렬
            tmp = defaultdict(int)
            for j in range(len(nums[i])): # 인덱스를 숫자로 취급해서 몇개인지 세아리기
                tmp[nums[i][j]] += 1 # 몇개 들어있는지 카운트
            tmp = sorted(tmp.items(), key=lambda x:(x[1], x[0]))
            nums[i] = []
            for j in range(len(tmp)):
                if tmp[j][0] == 0:
                    continue
                nums[i].append(tmp[j][0]) # 숫자와
                nums[i].append(tmp[j][1]) # 몇개인지 
        maxlen = -1
        for i in range(len(nums)):
            maxlen = max(maxlen, len(nums[i]))

        for i in range(len(nums)):
            for j in range(maxlen-len(nums[i])):
                nums[i].append(0)
    # C
    else:
        # print("C")
        nums = list(zip(*nums))
        for i in range(len(nums)): #행 별로 정렬
            tmp = defaultdict(int)
            for j in range(len(nums[i])): # 인덱스를 숫자로 취급해서 몇개인지 세아리기
                tmp[nums[i][j]] += 1 # 몇개 들어있는지 카운트
            tmp = sorted(tmp.items(), key=lambda x:(x[1], x[0]))
            nums[i] = []
            for j in range(len(tmp)):
                if tmp[j][0] == 0:
                    continue
                nums[i].append(tmp[j][0]) # 숫자와
                nums[i].append(tmp[j][1]) # 몇개인지 
        maxlen = -1
        for i in range(len(nums)):
            maxlen = max(maxlen, len(nums[i]))

        for i in range(len(nums)):
            for j in range(maxlen-len(nums[i])):
                nums[i].append(0)
        nums = list(zip(*nums))




    # for i in range(len(nums)):
    #     print(nums[i])
    time += 1

if flag:
    print(time)
else:
    print(-1)