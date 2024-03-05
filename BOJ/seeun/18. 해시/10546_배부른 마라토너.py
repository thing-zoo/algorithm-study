from collections import defaultdict
import sys
input = sys.stdin.readline
n = int(input())
dic = defaultdict(int)
for _ in range(n):
    dic[input().rstrip()] += 1 # 동명이인이 있을수도 있기 때문에 이름 별 참가인원수 체크

for _ in range(n-1):
    dic[input().rstrip()] -= 1 # 이름 별로 완주한 숫자 체크

for k in dic.keys():
    if dic[k] != 0: # 아직 완주 안한 사람이 있으면
        print(k) # 출력
        break