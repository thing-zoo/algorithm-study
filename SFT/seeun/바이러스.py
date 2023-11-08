import sys, math
k, p, n = map(int, input().split())
num = 1
for _ in range(n):
    num = (num%1000000007) * p # 10**8이라 숫자가 너무 커지기 때문에 처음부터 나머지로 연산해야함 -> 아니면 시간초과
print(int((k*num)%1000000007))