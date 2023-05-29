import sys
input = sys.stdin.readline
s, e, q = input().rstrip().split()
s = int(s[:2]) * 100 + int(s[3:])
e = int(e[:2]) * 100 + int(e[3:])
q = int(q[:2]) * 100 + int(q[3:])

stud = {}

while True:
    try:
        time, name = input().rstrip().split()
        time = int(time[:2]) *100 +  int(time[3:])
        if time <= s and name not in stud.keys(): # 시간 전에 왔고 아직 안왔었으면
            stud[name] = True
        elif time>=e and time<=q and name in stud.keys() and stud[name]: # 마친후, 스트리밍 끝내기 전에, 그리고 출석이 확인이 됐으면
            stud[name] = False
    except:
        break

print(list(stud.values()).count(False))