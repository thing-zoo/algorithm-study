import sys
from collections import defaultdict
input = sys.stdin.readline
plants = []
tmp = input().rstrip()

# 마지막 까지 입력받기
while tmp:
    plants.append(tmp)
    try:
        tmp = input().rstrip()
    except EOFError:
        break

p = defaultdict(int)
cnt = len(plants) # 전체 식물 개수
for plant in plants: # 종류별로 개수 세기
    p[plant] += 1

for k in p.keys(): # 식물 별로 차지하는 비중 계산
    p[k] = p[k]/cnt*100

key = sorted(list(p.keys())) # 오름차순 정렬
for k in key:
    print(k, end=" ")
    print('%.4f' %p[k])