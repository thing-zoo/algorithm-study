data = [ i for i in range(1, 21) ]

for i in range(10):
    a, b = map(int, input().split())
    data[a-1:b] = reversed(data[a-1:b])
print(*data)