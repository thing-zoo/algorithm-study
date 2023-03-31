from collections import deque

queue = deque()
visited = [False] * 300001
road = [0] * 300001

def bfs(i, j):
    prevtime = 0
    time = 0
    visited[i] = True
    queue.append([i, time])
    road[i] = 1

    while True:
        for _ in range(len(queue)):
            now, nowtime = queue.popleft()
            if now == j :
                return nowtime 

            if now*2<= 100000 and not visited[2*now]: # 순간이동은 time이 늘어나지 않기 때문에 걷는 것 보다 빨리 넣어야 정답이 나옴. 이유는? 몰라
                visited[now*2] = True
                queue.append([now*2, nowtime])
            if now-1>=0 and not visited[now - 1]:
                visited[now -1] = True
                queue.append([now-1, nowtime+1])
               
            if now+1<=100000 and not visited[now + 1] :
                visited[now +1] = True
                queue.append([now+1, nowtime+1])


me, bro = map(int, input().split())

if me == bro:
    print(0)
else:
    print(bfs(me, bro))
