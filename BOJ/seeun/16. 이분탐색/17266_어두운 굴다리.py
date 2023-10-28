n = int(input())
m = int(input())
loc = [0] + list(map(int, input().split())) + [n]
loc.sort()

# 가로등의 최소/최대 높이
s = 0
e = n

def binary_search(mid):
    # 1, 2번째  가로등의 간격이 m보다 크면 m이 더 넓어야됨
    if loc[1] - loc[0] > mid:
        return 0

    # 마지막 두개의 가로등 간격이 m보다 넓으면 m이 더 넓어야됨
    if loc[-1] - loc[-2] > mid:
        return 0
    
    for i in range(1, m):
        if (loc[i] - loc[i-1])/2 > mid:
            return 0
    
    # 모든 간격이 m보다 작거나 같으면 가로등 높이가 m이어도 됨
    return 1

ans = 0
while s<=e:
    mid = (s+e)//2
    if binary_search(mid): # 현재 가로등 높이로 모든 거리 커버 가능하면
        e = mid - 1 # 가로등 높이 더 낮게 도전
        ans = mid # 정답 갱신
    else: # 현재 가로등 높이가 너무 낮아서 모든 거리 커버 못하면
        s = mid + 1

print(ans)