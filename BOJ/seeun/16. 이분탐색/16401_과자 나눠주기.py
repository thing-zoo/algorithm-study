m, n = map(int, input().split())
snack = list(map(int, input().split()))
s = 1
e = max(snack)
res = 0
while s<=e:
    mid = (s+e)//2
    cnt = 0
    for i in range(n):
        cnt += (snack[i] // mid) # 각 과자를 중앙에 있는 과자 길이로 만들기
    if cnt >= m: # 길이가 m인 과자가 충분히 만들어지면
        res = max(mid, res)  # 일단 지금 과자 길이 저장
        s = mid +1 # 더 길게 만들어보기
    else:
        e = mid-1
print(res)