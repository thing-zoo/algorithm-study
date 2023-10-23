n, m = map(int, input().split())
visited = [False] * (n+1)
arr = []

def perm(cnt):
    if cnt == m:
        print(" ".join(map(str, arr)))
        return
    
    for i in range(1, n+1):
        if not visited[i]:
            visited[i] = True
            arr.append(i)
            perm(cnt + 1)
            visited[i] = False
            arr.pop()

perm(0)