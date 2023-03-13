import sys
n = int(sys.stdin.readline())
stack = []
result = []
cur = 1
flag = 0
for _ in range(n):
    data = int(sys.stdin.readline())
    while cur <= data: #입력한 수까지 오름차순 푸시
        stack.append(cur)
        result.append("+")
        cur += 1 #다음수부터 입력하도록 표시

    if data == stack[-1]: #top이면 pop    
        stack.pop()
        result.append("-")
    else:
        print("NO")
        flag = 1
        break

if flag == 0:
    for i in result:
        print(i)