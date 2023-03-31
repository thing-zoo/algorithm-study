from collections import deque

n, m = map(int, input().split())
deq = deque([i for i in range(n)])

nums = list(map(int, input().split()))

cnt = 0
for i in range(m):

    if deq.index(nums[i]-1) < len(deq)/2:
        while deq[0] != nums[i]-1:
            tmp = deq.popleft()
            deq.append(tmp)
            cnt += 1
           
    else:
        while deq[0] != nums[i]-1:
            tmp = deq.pop()
            deq.appendleft(tmp)
            cnt += 1
          
    deq.popleft()
        
print(cnt)