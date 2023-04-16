def dfs(i, sum):
    global add, sub, mul, div, max_value, min_value
    if i == n - 1: # n-1개의 연산자를 모두 선택했다면
        max_value = max(sum, max_value)
        min_value = min(sum, min_value)
        return # 종료
    if add > 0: # 연산자의 개수가 남아있다면
        add -= 1
        dfs(i+1, sum+a[i+1])
        add += 1
    if sub > 0:
        sub -= 1
        dfs(i+1, sum-a[i+1])
        sub += 1
    if mul > 0:
        mul -= 1
        dfs(i+1, sum*a[i+1])
        mul += 1
    if div > 0:
        div -= 1
        dfs(i+1, int(sum/a[i+1]))
        div += 1
        
n = int(input())
a = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())
max_value = -1e9
min_value = 1e9
dfs(0, a[0])
print(max_value)
print(min_value)