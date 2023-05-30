import sys
input = sys.stdin.readline
k, l = map(int, input().rstrip().split())
d = {}
for i in range(l):
    number = input()
    if number not in d:
        d[number] = i
    else:
        d[number] = i
result = sorted(d.items(), key=lambda x: x[1])[:k]
for number, _ in result:
    sys.stdout.write(number)