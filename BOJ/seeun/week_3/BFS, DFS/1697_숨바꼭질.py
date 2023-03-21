from collections import deque

queue = deque()
visited = [False] * 300001
road = [0] * 300001

def bfs(i, j):
    time = 0
    visited[i] = True
    queue.append([i, time])
    road[i] = 1

    while True:
        
        time += 1
        for _ in range(len(queue)):
            now, nowtime = queue.popleft()
            if now -1 == j or now +1 == j or 2*now == j :
                return time 

            if now-1>=0 and not visited[now - 1]:
                visited[now -1] = True
                queue.append([now-1, time])
               
            if now+1<=100000 and not visited[now + 1] :
                visited[now +1] = True
                queue.append([now+1, time])

            if now*2<= 100000 and not visited[2*now]:
                visited[now*2] = True
                queue.append([now*2, time])


me, bro = map(int, input().split())

if me == bro:
    print(0)
else:
    print(bfs(me, bro))
