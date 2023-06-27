import sys
input = sys.stdin.readline
def find(x):
    global parent
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    global cycle, parent
    a = find(a)
    b = find(b)
    if a != b:
        if a > b:
            a, b = b, a
        parent[b] = a

n, m = map(int, input().rstrip().split())
cnt = 0
while n != 0 or m!= 0:
    cnt += 1
    parent = [i for i in range(n+1)]
    cycle = []
    for _ in range(m):
        a, b = map(int, input().rstrip().split())
        pa, pb = find(a), find(b)
        if pa!=pb:
            union(a, b)
        else: # 두개를 이을건데 두개의 부모가 같으면 사이클임
            cycle.append(pa) # 이 노드는 사이클에 포함됨
            cycle.append(pb)

    # 사이클에 포함되는 노드들의 루트 갱신    
    for i in range(len(cycle)): 
        cycle[i] = find(cycle[i])

    ans = 0
    cycle = set(cycle) # 중복 제거
    for i in range(1, n+1): # n개의 노드를 검사하면서 사이클에 포함인지 검사
        mom = find(i) 
        if mom in cycle: 
            continue
        # 사이클에 포함 안되면 정답 +1 하고 해당 노드를 사이클에 있다고 침 (다시 검사 안하기 위해서)
        ans += 1
        cycle.add(mom)

    if ans > 1:
        print('Case ',  cnt, ': A forest of ' ,ans, ' trees.', sep="")
    elif ans == 1:
        print('Case ',  cnt, ': There is one tree.', sep="")
    else:
        print('Case ',  cnt, ': No trees.' ,sep="")
    
    n, m = map(int, input().rstrip().split())

