n, m = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))
c = sorted(list(a - b))
if c:
    print(len(c))
    print(' '.join(map(str, c)))
else:
    print(0)