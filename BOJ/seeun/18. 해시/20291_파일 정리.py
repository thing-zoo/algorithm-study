import sys
from collections import defaultdict
input = sys.stdin.readline
n = int(input())
files = [input().rstrip() for _ in range(n)] # 파일 입력 받기
dic = defaultdict(int)

for i in range(n):
    name, ext = files[i].split('.') # .을 기준으로 파일이름, 확장자로 나누기
    dic[ext] += 1 # 해당확장자 개수 +1

ext_list = sorted(list(dic.keys())) # key만 리스트로 변환 후 정렬
for e in ext_list:
    print(e, dic[e])