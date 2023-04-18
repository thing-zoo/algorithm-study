import sys
input = sys.stdin.readline
n = int(input())
data = [ list(input().strip().split()) for _ in range(n) ] # 이름(0), 국어(1), 영어(2), 수학(3)
for e in sorted(data, key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0])):
    sys.stdout.write(e[0]+'\n')