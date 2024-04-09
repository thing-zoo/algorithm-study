a, b, c, d, e, f = map(int, input().split())

# 수학 풀이
# x = (b*f-e*c)//(b*d-a*e)
# y = (a*f-d*c)//(a*e-d*b)
# print(x, y)

# 완탐 풀이
for x in range(-999, 1000):
    for y in range(-999, 1000):
        if a*x + b*y == c and d*x + e*y == f:
            print(x, y)
            break