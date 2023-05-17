n = int(input())
nums = list(map(int, input().split()))
nums.sort()
cnt = 0
if n <3:
    print(0)

else:
    for i in range(n):
        res = nums[i]
        s = 0
        e = n-1
        while s<e:
            if nums[s] + nums[e] == res and s != i and e != i: # 자기 자신이면 안되는 조건 있어야함
                cnt += 1
                break # 그 숫자가 좋은 숫자인지는 한개의 경우만 확인해도 되기 때문에 한번 확인하면 바로 break
            elif nums[s] + nums[e] < res:
                s += 1
            else:
                e -= 1
                
            if s == i: # 자기자신이면 안됨
                s += 1
            elif e == i:
                e -= 1
    print(cnt)