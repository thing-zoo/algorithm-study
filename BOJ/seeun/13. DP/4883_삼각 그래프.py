import sys
input = sys.stdin.readline

cnt = 1
n = int(input())
while n!=0:
    graph = []
    for i in range(n):
        graph.append(list(map(int, input().rstrip().split())))
    graph[0][0] = 1000000 #[0][0]에서 [1][0]으로 갈 수는 없음
    graph[0][2] += graph[0][1] #[0][2] 값 초기화
    for i in range(1, n):
        graph[i][0] += min(graph[i-1][0], graph[i-1][1])
        graph[i][1] += min(graph[i-1][0], graph[i-1][1], graph[i-1][2], graph[i][0])
        graph[i][2] += min(graph[i-1][1], graph[i-1][2], graph[i][1])
    print(cnt, ". ", graph[n-1][1],sep="")
    cnt += 1
    n = int(input())