from collections import deque
f, s, g, u, d = map(int, input().split())

visited = [0]*(f+1)
cnt = 0
queue = deque()

def bfs(s):
    global f,g, u, d, cnt
    queue.append([s, cnt])
    visited[s] = 1
    while queue:
        tmp, cnt = queue.popleft()
        if tmp == g: # 도착하면 리턴트루
            return cnt
     
        cnt +=1
        if 1<=(tmp + u) <= f and visited[tmp+u] == 0 :
            visited[tmp+u] =1
            queue.append([tmp+u, cnt])

        if f>=(tmp-d)>=1 and visited[tmp-d] == 0: # 범위 내에 있고 방문 안했으면
            visited[tmp-d] =1
            queue.append([tmp-d, cnt])
            
    return "use the stairs"

print(bfs(s))