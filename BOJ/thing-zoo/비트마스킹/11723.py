import sys
input = sys.stdin.readline
s = 0
for _ in range(int(input())):
    data = list(input().strip().split())
    if data[0] == 'add':
        x = int(data[1])
        s |= (1 << x)
    elif data[0] == 'remove':
        x = int(data[1])
        s &= ~(1 << x)
    elif data[0] == 'check':
        x = int(data[1])
        if s & (1 << x): sys.stdout.write('1\n')
        else: sys.stdout.write('0\n')
    elif data[0] == 'all':
        s = (1 << 21) - 1
    elif data[0] == 'toggle':
        x = int(data[1])
        s ^= (1 << x)
    else: # empty
        s = 0