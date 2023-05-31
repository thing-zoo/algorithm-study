def solution(i):
    if i not in a:
        a[i] = solution(i//p) + solution(i//q)
    return a[i]
n, p, q = map(int, input().split())
a = {0: 1}
print(solution(n))