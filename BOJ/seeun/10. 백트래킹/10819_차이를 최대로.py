n = int(input())
nums = list(map(int, input().split()))

def calcul(arr): # 주어진 공식에 맞게 계산
    tmp = 0
    for i in range(n-1):
        tmp += abs(arr[i]-arr[i+1])
    return tmp

def perm(cnt): # 순열로 숫자들의 순서를 정함
    global ans

    if cnt == n: # 모든 숫자를 골랐으면
        tmp = calcul(arr)
        ans = max(ans, tmp) # 정답 갱신
        return

    for i in range(n):
        if not visited[i]:
            arr.append(nums[i])
            visited[i] = True
            perm(cnt+1)
            visited[i] = False
            arr.pop()

arr = []
ans = 0
visited = [False] * n
perm(0)
print(ans)