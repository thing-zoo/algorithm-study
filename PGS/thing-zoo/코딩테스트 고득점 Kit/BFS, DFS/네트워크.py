from collections import deque
def bfs(v, visited):
    q = deque()
    q.append(v)
    visited[v] = True
    while q:
        v = q.popleft()
        for i, w in enumerate(computers[v]):
            if i == v: continue
            if w == 1 and not visited[i]:
                visited[i] = True
                q.append(i)


def solution(n, computers):
    answer = 0
    visited = [False]*n
    for i in range(n):
        if not visited[i]:
            bfs(i, visited)
            answer += 1

    return answer
n = 3
computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
print(solution(n, computers))