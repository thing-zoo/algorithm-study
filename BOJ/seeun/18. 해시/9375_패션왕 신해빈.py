from collections import defaultdict
from itertools import combinations
import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    cloth = defaultdict(int)
    for _ in range(n):
        clo, cate =input().rstrip().split()
        cloth[cate] += 1
    cnt = 1

    for i in cloth.values():
        cnt *= (i+1)
    
    print(cnt-1)