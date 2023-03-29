def solution(n, computers):
    answer = 0
    network = [[] for _ in range(n)]
    visited = [0]*n
    visited[0] = 1
    for i in range(n):
        for j in range(i+1, n):
            if computers[i][j] and not visited[j]:
                network[i].append(j)
                visited[j] = 1

    return answer
n = 3
computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
print(solution(n, computers))