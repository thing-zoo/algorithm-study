import bisect
import sys
input = sys.stdin.readline

A, B, C, D = [], [], [], []
for _ in range(int(input())):
    a, b, c, d = map(int, input().strip().split())
    A.append(a); B.append(b); C.append(c); D.append(d)

ab = {}
for a in A:
    for b in B:
        if a + b not in ab.keys():
            ab[a + b] = 1
        else:
            ab[a + b] += 1

answer = 0
for c in C:
    for d in D:
        if -c-d in ab.keys():
            answer += ab[-c-d]
print(answer)