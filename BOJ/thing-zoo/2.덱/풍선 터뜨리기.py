from collections import deque
n = int(input())
ballon = deque([i for i in range(1, n+1)]) # 풍선 번호
paper = deque(list(map(int, input().split()))) # 종이 값
answer = []
while ballon:
    i = ballon.popleft()
    j = paper.popleft()
    if j > 0: j -= 1
    ballon.rotate(-j) # 뒤로 j개 보내기
    paper.rotate(-j)
    answer.append(i)
print(' '.join(map(str, answer)))