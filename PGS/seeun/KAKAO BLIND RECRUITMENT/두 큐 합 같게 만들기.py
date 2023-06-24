from collections import deque
def solution(queue1, queue2):
    answer = -2
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    
    cnt = 0
    total = sum1 + sum2
    limit = len(queue1) + len(queue2) # 큐에서 이동 횟수 한계
    
    if total % 2 == 1: # 홀수이면 불가능함
        return -1

    while sum1 != sum2:
        if cnt > limit:
            return -1

        while queue2 and sum1 < sum2:
            move = queue2.popleft()
            queue1.append(move)
            sum1 += move
            sum2 -= move
            cnt += 1
        
        while queue1 and sum2 < sum1:
            move = queue1.popleft()
            queue2.append(move)
            sum2 += move
            sum1 -= move
            cnt += 1
        
    answer = cnt
    return answer