n, m = map(int, input().split()) # 나무 n개, 원하는 나무 길이 m
trees = sorted(list(map(int, input().split())), reverse=True) # 나무의 높이
answer = 0 # 절단기 설정 높이의 최댓값
start = 1
end = trees[0]
while start <= end:
    mid = (start + end)//2
    count = 0 # 자른 나무의 높이의 합
    for tree in trees:
        count += tree - mid
        if count >= m: break
    if count >= m:
        answer = max(answer, mid)
        start = mid + 1
    else:
        end = mid - 1
print(answer)