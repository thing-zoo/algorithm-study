n = int(input())
students = list(map(int, input().split()))
b, c = map(int, input().split())

result = n
for a in students:
    a -= b
    if a <= 0: continue
    if a % c: result += a//c + 1
    else: result += a//c
print(result)