from collections import deque

gear1 = deque(list(map(int, list(input()))))
gear2 = deque(list(map(int, list(input()))))
gear3 = deque(list(map(int, list(input()))))
gear4 = deque(list(map(int, list(input()))))
gears = [gear1, gear2, gear3, gear4]

n = int(input())

for _ in range(n):
    s = [False]*3
    g, dir = map(int, input().split())
    g = g-1
    # i와 i+1번째 톱니가 서로 다른 극인지 체크
    if gear1[2] != gear2[6]:
        s[0] = True
    if gear2[2] != gear3[6]:
        s[1] = True
    if gear3[2] != gear4[6]:
        s[2] = True

    # 첫번째 기준이 되는 톱니 회전
    if dir == -1: # 반시계
        gears[g].append(gears[g].popleft())
    else: # 시계
        gears[g].appendleft(gears[g].pop())

    # 기준 톱니의 회전 방향 저장
    tempdir = dir

    # 기준 톱니의 왼쪽 톱니 돌리기
    for i in range(g-1, -1, -1):
        tempdir *= -1
        if s[i]:
            if tempdir == -1: # 반시계
                gears[i].append(gears[i].popleft())
            else: # 시계
                gears[i].appendleft(gears[i].pop())
        else: # 하나라도 안 돌면 그 옆에것도 못 돎
            break 

    # 기준 톱니의 오른쪽 톱니 돌리기
    tempdir = dir
    for i in range(g, 3, 1):
        tempdir *= -1
        if s[i]:
            if tempdir == -1: # 반시계
                gears[i+1].append(gears[i+1].popleft())
            else: # 시계
                gears[i+1].appendleft(gears[i+1].pop())
        else: # 하나라도 안 돌면 그 옆에것도 못돎
            break

print(gear1[0]*1 + gear2[0]*2 + gear3[0]*4 + gear4[0]*8)