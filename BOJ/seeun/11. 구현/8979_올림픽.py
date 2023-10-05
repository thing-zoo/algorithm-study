import sys
input = sys.stdin.readline
n, k = map(int, input().split())
info = {}
for _ in range(n):
    medal = list(map(int, input().split()))
    info[medal[0]] = medal[1:]

sorted_info = sorted(info.values(), key=lambda x:(-x[0], -x[1], -x[2])) # 메달 정보만 금은동 순으로 정렬
medal = info[k] # 등수 찾을 나라의 메달 정보
print(sorted_info.index(medal)+1) # 메달 정보가 몇번째에 있는지
