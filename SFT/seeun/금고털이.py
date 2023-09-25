import sys
input = sys.stdin.readline
n, m = map(int, input().split())
jew = []
for _ in range(m):
    jew.append(list(map(int, input().split())))

# 보석을 잘라서 넣을 수 있으므로 무게당 가치가 가장 높은 순서대로 정렬
jew.sort(key=lambda x:-x[1])
bag = 0 # 현재 가방에 담은 보석의 무게
value = 0 # 현재 담긴 보석들의 가치
for j in jew:
    if n-bag > j[0]: # 남은 공간이 현재 보석무게 보다 크면
        bag += j[0] # 바로 담기
        value += j[0]*j[1] # 무게*가치
    else: # 남은 만큼만 넣을 수 있음
        value += (n-bag)*j[1] 
        bag += (n-bag) # 넣을 수 있는 만큼만 잘라서 넣음
    if bag == n: # 가방이 가득 찼으면 중단
        break
print(value)