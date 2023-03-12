from os import sep


n, kill = map(int, input().split())
num = [i+1 for i in range(n)]

idx = kill-1
res = []
while True:
    print(num)
    res.append(num.pop(idx))
    if len(num)==0:
        break
    idx = (idx+kill-1)%len(num)

print("<", end="")
print(*res, sep=", ", end="")
print(">")