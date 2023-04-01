n, x = map(int, input().split())

data = list(map(int, input().split()))

for i in range(n):
    a = data[i]
    if a < x:
        print(a, end=" ")