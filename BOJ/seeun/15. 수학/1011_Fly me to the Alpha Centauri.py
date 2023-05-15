t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    dist = b-a
    cnt = 0

    move = 1 # 이동할 수 있는 거리
    move_dist = 0 # 이동한 거리
    while move_dist < dist:
        cnt += 1
        move_dist += move
        if cnt % 2 == 0:
            move += 1
        
    print(cnt)