n = int(input())
nums = list(map(int, input().split()))

stack = [nums[0]]
for i in range(1, n):
    if stack[-1] < nums[i]: # 스택 탑이 현재 숫자보다 작으면 그냥 삽입
        stack.append(nums[i])
    else: # 현재 숫자가 더 작으면 숫자를 덮어쓰러 감
        s = 0
        e = len(stack)-1
        while s<=e:
            m = (s+e)//2
            if stack[m] == nums[i]: # 똑같은 숫자를 찾으면 그 자리에 덮어쓰기
                s = m
                break
            elif stack[m] < nums[i]:
                s = m+1
            else:
                e = m-1
        stack[s] = nums[i] # nums[i]보다 큰 숫자들 중에 가장 작은 숫자를 덮어쓰기 
    # print(stack)
print(len(stack))