from collections import deque
n = int(input())
num = deque(list(map(int, input().split())))
balloon = deque([i for i in range(1, n+1)])

for _ in range(n):
    paper = num.popleft() # 풍선 안에 들어있는 종이
    ball = balloon.popleft() # 풍선 번호
    print(ball, end=" ") # 터진 풍선 번호 출력

    if not num: # 다 터졌으면 종료
        break

    if paper > 0: # 오른쪽으로 이동
        for _ in range(paper-1):
            num.append(num.popleft())
            balloon.append(balloon.popleft())
    else: # 왼쪽으로 이동
        paper *= -1 # 양수로 만들기
        for _ in range(paper):
            num.appendleft(num.pop())
            balloon.appendleft(balloon.pop())