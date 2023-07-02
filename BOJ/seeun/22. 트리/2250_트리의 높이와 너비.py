import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline
n = int(input().rstrip())
tree = [[] for _ in range(n+1)]

def dfs(node, level): # 중위순회를 통해 트리 탐색
    global col, board
    if node == -1:
        return
    dfs(tree[node][0], level+1) # 왼쪽노드 방문
    board[level].append(col) # 현재 노드를 레벨에 맞게 격자에 표시
    col += 1 # 열 한칸 옮김
    dfs(tree[node][1], level+1) # 오른쪽노드 방문

root = n*(n+1) //2 # 모든 노드의 값 더하기
for _ in range(n):
    a, b, c = map(int, input().rstrip().split())
    tree[a].append(b)
    tree[a].append(c)
    # 자식으로 불려진 노드들을 root 값에서 빼줌 -> 남은 값이 루트노드임
    if b != -1:
        root -= b
    if c != -1:
        root -= c

board = [[] for _ in range(n + 1)]
col = 0
dfs(root, 1)

maxlevel = -1
maxlength = -1
for i in range(1, n+1):
    if not board[i]: # 빈 행이면 끝내도 됨
        break
    start = min(board[i])
    end = max(board[i])

    if maxlength < end - start +1:
        maxlength = end - start + 1
        maxlevel = i
print(maxlevel, maxlength)
    