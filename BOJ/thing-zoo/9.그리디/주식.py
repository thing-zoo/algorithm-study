import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    stocks = list(map(int, input().rstrip().split()))
    profit = 0
    max_stock = stocks[-1]
    for i in range(n-1, -1, -1):
        if stocks[i] > max_stock:
            max_stock = stocks[i]
        else:
            profit += max_stock - stocks[i]
    sys.stdout.write("%d\n" %profit)