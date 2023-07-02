import sys
input = sys.stdin.readline

def find(x):
    global parent
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if x<y:
        parent[y] = x
    else:
        parent[x] = y

n, m = map(int, input().rstrip().split())
parent = [i for i in range(n+1)]
answer = 0 # 끊거나 연결하는 횟수

for _ in range(m):
    x, y = map(int, input().rstrip().split())
    px = find(x)
    py = find(y)
    if px != py:
        union(x, y)
    else: # 루트가 같으면 사이클임 => 끊어줘야함
       answer += 1
       union(x, y)

tmp = [] # 존재하는 루트들을 저장
for i in range(1, n+1):
    pi = find(i)
    if tmp and pi in tmp: # 루트가 이미 있으면
        continue
    else: # 아직 이어지지 못한 루트이면 연결해야함
        tmp.append(pi)

print(answer+len(tmp)-1)
