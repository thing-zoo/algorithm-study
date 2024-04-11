t = int(input())
for _ in range(t):
    n = int(input())
    data = sorted(list(map(int, input().split())))
    print(data[0], data[-1])