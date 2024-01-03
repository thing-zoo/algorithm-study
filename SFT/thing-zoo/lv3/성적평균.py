n, k = map(int, input().split())
scores = list(map(int, input().split()))
for _ in range(k):
    a, b = map(int, input().split())
    print('%2.2f' %round(sum(scores[a-1:b])/(b-a+1), 2))