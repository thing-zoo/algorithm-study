import sys
from collections import defaultdict
input = sys.stdin.readline # 시간초과로 인해 변경
trees = defaultdict(int)
total = 0
while True:
    tree = input().rstrip()
    if tree == '': # input과 달리 EOFError 발생시키지 않고, 빈문자열 반환
        break
    trees[tree] += 1
    total += 1
for tree in sorted(trees.keys()):
    print(f'{tree} {trees[tree]/total*100:.4f}')