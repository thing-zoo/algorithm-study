# x/n=y...y
# x=n*y+y
# x=(n+1)*y, (0<y<n)
n = int(input())
total = 0
for i in range(1, n):
    total += i*(n+1)
print(total)