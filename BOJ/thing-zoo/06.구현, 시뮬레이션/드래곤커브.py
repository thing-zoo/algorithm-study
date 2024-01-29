def count_square():  # 정사각형 세는 함수
    answer = 0
    for i in range(100):
        for j in range(100):
            if graph[i][j] and graph[i][j+1] and graph[i+1][j] and graph[i+1][j+1]:
                answer += 1
    print(answer)

def dragon_curve():  # 드래곤 커브를 그리는 함수
    x, y, d, g = map(int, input().split())
    # 0세대
    graph[y][x] = 1  # 방문 표시
    nx, ny = x, y
    nx += dx[d]; ny += dy[d]
    if 0 <= nx < 101 and 0 <= ny < 101:
        graph[ny][nx] = 1

    dir = [d]
    for i in range(g):  # 세대만큼 반복
        next_dir = list(map(lambda d: (d+1) % 4, dir))  # 90도 회전
        for d in next_dir:
            nx += dx[d]; ny += dy[d]
            if 0 <= nx < 101 and 0 <= ny < 101:
                graph[ny][nx] = 1
        dir = next_dir[::-1] + dir

dx = [1, 0, -1, 0]; dy = [0, -1, 0, 1]
graph = [[0]*101 for _ in range(101)]
n = int(input())
for _ in range(n):
    dragon_curve()
count_square()