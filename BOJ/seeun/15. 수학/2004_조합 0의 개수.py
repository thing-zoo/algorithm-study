n, m = map(int, input().split())

def cal(n, k):
    cnt = 0
    while n:
        cnt += n//k
        n //= k
    return cnt

print(min(cal(n, 2)-cal(m, 2)-cal(n-m, 2), cal(n, 5)-cal(m, 5)-cal(n-m, 5)))