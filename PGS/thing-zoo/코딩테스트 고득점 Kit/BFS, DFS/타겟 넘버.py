from collections import deque
def solution(numbers, target):
    q = deque([0])
    while numbers:
        for _ in range(len(q)):
            x = q.popleft()
            i = numbers[-1]
            for j in (1, -1):
                nx = x + i*j
                q.append(nx)
        numbers.pop()
    return q.count(target)
numbers = [1,1,1,1,1]
target = 3
print(solution(numbers, target))