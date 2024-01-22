from collections import defaultdict
def dfs(u, outs, visited):
    visited[u] = True
    for v in outs[u]:
        if not visited[v]:
            visited[v] = True
            dfs(v, outs, visited)

def check(nodes, ins, outs):
    root = 0
    count = 0
    visited = {}
    if len(nodes) == 0: # 빈 트리
        return True
    for i in nodes:
        visited[i] = False
        if i not in ins: # 들어오는 간선이 없는 루트
            count += 1
            root = i
        elif len(ins[i]) != 1: # 루트 외는 반드시 들어오는 간선 하나
            return False
    if count != 1: # 루트가 하나인지 확인
        return False
    
    # 루트에서 다른노드로 가는 경로 확인
    dfs(root, outs, visited)
    if False in visited.values():
        return False
    
    return True

def solution():
    ins = defaultdict(list) # 들어오는 간선
    outs = defaultdict(list) # 나가는 간선
    nodes = set() # 정점들
    n = 1 # 테케 순번
    while True:
        line = list(map(int, input().split()))
        for i in range(0, len(line), 2):
            u, v = line[i], line[i+1]
            if u == v == -1:
                return
            if u == v == 0:
                if check(nodes, ins, outs):
                    print(f'Case {n} is a tree.')
                else:
                    print(f'Case {n} is not a tree.')
                n += 1
                ins = defaultdict(list)
                outs = defaultdict(list)
                nodes = set()
            else:
                nodes.add(u)
                nodes.add(v)
                outs[u] += [v]
                ins[v] += [u]

solution()