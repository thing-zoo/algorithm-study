import sys
string = list(sys.stdin.readline().strip())
n = int(sys.stdin.readline())

origin = string
temp = [] # 커서 이동에 따라 옮겨 담아둘 스택

for i in range(n):
    cmd = sys.stdin.readline().strip()
    if len(cmd)>1:
        cmd, s = cmd.split()
    
    # 명령어 수행
    if cmd == "L": 
        if origin : # 왼쪽으로 한 칸 갈 수 있으면
            temp.append(origin.pop()) # 스택에 옮겨두기
    elif cmd == "D": # 오른족으로 갈 수 있는데
        if temp: # 커서 오른쪽에도 글자가 있으면
            origin.append(temp.pop()) # 다시 origin에 옮겨 담음
    elif cmd == "B": # 지울 거 있으면 그냥 지우기
        if origin:
            origin.pop()
    elif cmd == "P":
        origin.append(s)

while temp: # 커서가 중간에 있을 경우 temp 스택에 있는것들 다 옮겨 담기
    origin.append(temp.pop())
print(*origin, sep="")