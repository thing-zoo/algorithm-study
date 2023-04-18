import sys
input = sys.stdin.readline
def check(arr):
    total = 0
    for i in arr:
        if i.isdigit():
            total += int(i)
    return total

n = int(input())
data = [ input() for _ in range(n) ]
for e in sorted(data, key=lambda x: (len(x), check(x), x)):
    sys.stdout.write(e)