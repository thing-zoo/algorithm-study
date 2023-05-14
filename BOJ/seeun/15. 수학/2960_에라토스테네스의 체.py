n, k = map(int, input().split())
nums = list(range(n+1))

nums[0] = 9999
nums[1] = 9999
cnt = 0 # 횟수 카운트
while True:
    num = min(nums)
    i = 0

    while (i*num) < n+1:
        if nums[num*i] == 9999: # 이미 지워진 수이면 넘어가기
            i += 1
            continue
        cnt += 1

        if cnt == k: # k번째 지우는 숫자
            print(nums[num*i])
            break
        nums[num*i] = 9999 # 숫자 지워주기
        i += 1
    if cnt == k:
        break