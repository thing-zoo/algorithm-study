n, k = map(int, input().split())
coin = []
for _ in range(n):
    coin.append(int(input()))

coin.sort()
d = [0]*(k+1)
d[0] = 1
for i in coin:
    for j in range(i, k+1):
        # i동전을 썼을 때, j원을 i동전을 빼고 만들수 있는 경우의 수를 더함
        if j-i>=0:
            d[j] += d[j-i]
print(d[k])