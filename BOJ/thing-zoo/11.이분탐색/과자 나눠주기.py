m, n = map(int, input().split())
l = sorted(list(map(int, input().split())), reverse=True)
answer = 0 # 과자의 최대길이
start = 1
end = l[0]
while start <= end:
    mid = (start+end)//2
    count = 0
    for i in l:
        count += i//mid
        if count >= m:
            break
    if count >= m: # 모든 조카에게 나눠줄수있으면
        answer = max(answer, mid) # 길이 갱신
        start = mid + 1 # 더 큰수로
    else:
        end = mid - 1 # 더 작은수로
print(answer)