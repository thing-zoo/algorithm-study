n = int(input())
sign = list(input().split())
m = n + 1 # 고를 숫자의 개수

def check(arr):
    res = True
    for i in range(n):
        if sign[i] == '<':
            if arr[i] > arr[i+1]:
                res = False
                return res
        else:
            if arr[i] < arr[i+1]:
                res = False
                return res
    return res

def perm(cnt): # 순열로 숫자들의 순서를 정함
    global minans, maxans
    if cnt == m: # 모든 숫자를 골랐으면
        if check(arr):
            if int(minans) > int("".join(map(str, arr))):
                minans = "".join(map(str, arr))

            if int(maxans) < int("".join(map(str, arr))):
                maxans = "".join(map(str, arr))
        return

    for i in range(10):
        if not visited[i]:
            arr.append(i)
            visited[i] = True
            perm(cnt+1)
            visited[i] = False
            arr.pop()

arr = []
minans = '9999999999'
maxans = '0'
visited = [False]*10
perm(0)
print(maxans)
print(minans)