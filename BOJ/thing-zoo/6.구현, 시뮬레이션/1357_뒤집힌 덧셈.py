x, y = input().split()
x = str(int(x[::-1]) + int(y[::-1]))
x = int(x[::-1])
print(x)