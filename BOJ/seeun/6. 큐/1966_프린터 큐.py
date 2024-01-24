from collections import deque
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))
    queuen = deque() # 처음 큐 상황
    queuep = deque() # 우선순위
    for i in range(n):
        queuen.append(i)
        queuep.append(nums[i])
    cnt = 0

    while queuen:
        if queuep[0] >= max(queuep): # 제일 앞 프린트의 우선순위가 최댓값이면 출력
            queuep.popleft()
            tmp = queuen.popleft()
            cnt+= 1
            if tmp == m: # 출력한 프린트가 찾고자 하는 프린트이면
                print(cnt)
                break # 종료
        else: # 우선순위가 더 높은 프린트가 있으면 제일 뒤로 넘기기
            queuep.append(queuep.popleft())
            queuen.append(queuen.popleft())
            