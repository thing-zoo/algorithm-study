from itertools import combinations

def gcd(a, b):
    if a == 0: return b
    return gcd(b%a, a)

for _ in range(int(input())):
    data = list(map(int, input().split()))
    answer = 0
    for a, b in combinations(data[1:], 2):
        g = gcd(a, b)
        answer += g
    print(answer)