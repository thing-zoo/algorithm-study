n, p, q = map(int, input().split())
dict = {}

dict[0] = 1
def dfs(n):
    global dict
    if n in dict: # 이미 있는 숫자이면 그 숫자를 바로 리턴
        return dict[n]
    dict[n] = dfs(n//p) + dfs(n//q) # 필요한 숫자를 구하러 dfs
    return dict[n]

print(dfs(n))
# print(dict)