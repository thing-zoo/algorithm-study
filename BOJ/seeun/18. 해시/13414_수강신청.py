import sys
input = sys.stdin.readline
k, l = map(int, input().rstrip().split())

stud = {}
idx = 1

for i in range(l):
    stud[input().rstrip()] = idx
    idx += 1

stud = sorted(stud.items(), key=lambda x:x[1])
for i in range(min(k, len(stud))):
    print(stud[i][0])