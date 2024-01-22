def f(x, y):
    print(y-x-1)
    for i in range(x+1, y):
        print(i, end=" ")

a, b = map(int, input().split())
if b - a > 1:
    f(a, b)
elif 0 <= b - a <= 1:
    print(0)
else:
    f(b, a)