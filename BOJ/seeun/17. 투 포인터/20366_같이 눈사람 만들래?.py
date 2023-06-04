n = int(input())
nums = sorted(list(map(int, input().split())))

ans = 10e9-1

for l1 in range(n-3): # 엘사의 왼쪽포인터 지정
    for r1 in range(l1+3, n): # 엘사의 오른쪽 포인터 지정 - 둘 사이에 최소 2개의 숫자 보장
        elsa = nums[l1]+nums[r1]
        l2 = l1+1 # 안나 왼쪽: 엘사 왼쪽 +1 부터 시작
        r2 = r1-1 # 안나 오른쪽: 엘사 오른쪽 -1 부터 시작
        while l2 < r2:
            anna = nums[l2]+nums[r2]
            ans = min(ans, abs(elsa-anna)) # 차이가 더 작은 값 선택
            if abs(elsa) < abs(anna): # 안나의 값이 더 크면 오른쪽 포인터 줄이기
                r2 -= 1
            elif abs(elsa) > abs(anna): # 안나가 더 작으면 왼쪽 포인터 증가시키기
                l2 += 1
            else:
                break
        if ans == 0:
            break
    if ans == 0:
        break
print(ans)