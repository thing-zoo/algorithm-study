from collections import deque
def solution(a):
    bridge = deque([0]*w)
    a = deque(a)
    sum = 0
    time = 0
    while bridge:
        sum -= bridge.popleft()
        if a:
            if sum + a[0] <= L: 
                sum += a[0]
                bridge.append(a.popleft())
            else: bridge.append(0)
        time += 1
    return time

# n: 다리를 건너는 트럭의 수, w: 다리의 길이, L: 다리의 최대하중
# a: 트럭의 무게
n, w, L = map(int, input().split())
a = map(int, input().split())
print(solution(a))