n, m = map(int, input().split())

visited = [False]*(n+1) # 1~N 숫자 방문 체크
arr = [0]*m # 길이 M인 수열 저장하는 배열

def btk(cnt):
    if cnt == m: # M개의 숫자 다 골랐으면 출력
        for i in arr:
            print(i, end=" ")
        print()
        return
    
    for i in range(1, n+1): # 1~N까지의 수
        if not visited[i]:
            visited[i] = True
            arr[cnt] = i
            btk(cnt+1)
            visited[i] = False

btk(0)