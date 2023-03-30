from collections import deque
def solution(tickets):
    answer = []
    n = len(tickets)
    visited = [False]*n
    q = deque([[["ICN"], visited]])
    while q:
        route, visited = q.popleft()
        if len(route) == n + 1:
            answer.append(route)
        for i, t in enumerate(tickets):
            if t[0] == route[-1] and not visited[i]: # 현재경로에서 연결된다면
                new_visited = visited[:]
                new_route = route[:]
                new_route.append(t[1]) # 현재경로에 추가
                new_visited[i] = True  # 현재경로에 대한 티켓 방문표시
                q.append([new_route, new_visited]) # 큐에 삽입
    answer.sort()
    return answer[0]
tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
print(solution(tickets))