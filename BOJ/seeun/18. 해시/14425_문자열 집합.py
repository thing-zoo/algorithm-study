import sys
input = sys.stdin.readline
n, m = map(int, input().rstrip().split())
S = {}
for _ in range(n):
    tmp = input().rstrip()
    S[tmp] = 0

cnt = 0
for _ in range(m):
    string = input().rstrip()
    if string in S.keys(): # 존재하는 key이면
        S[string] += 1 # 개수 +1
cnt = sum(list(S.values())) 
print(cnt)