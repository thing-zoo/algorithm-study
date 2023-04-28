n = int(input())
nums = list(map(int, input().split()))
d = [[] for _ in range(n+1)]
d[0].append(nums[0])
for i in range(1, n):
    for j in range(i+1): # 0~i 까지 돌면서 길이가 가장긴 배열을 찾아감
        if nums[j]<nums[i]:
            if len(d[j])+1 >= len(d[i]): #j배열에 나를 더한 것의 길이가 i보다 길면 바꿔주기
                d[i] = d[j][:]
                d[i].append(nums[i])
        else: # 앞 숫자들이 나보다 큰 숫자들이면
            if len(d[i]) < 1: # 근데 모두 다 나보다 크면 그냥 나 넣기
                d[i].append(nums[i])

# 길이를 기준으로 가장긴 값, 배열 출력
print(len(max(d, key=len)))
print(*max(d, key=len))