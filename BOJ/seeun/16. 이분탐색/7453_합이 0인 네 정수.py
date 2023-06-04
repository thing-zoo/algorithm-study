n = int(input())
nums = [list(map(int, input().split())) for _ in range(n)]
ab = []
cd = []
# 가능한 ab의 조합과 cd의 조합을 다 구해서 배열에 넣음
for i in range(n):
    for j in range(n):
        ab.append(nums[i][0] + nums[j][1])
        cd.append(nums[i][2] + nums[j][3])
ab.sort()
cd.sort()

cnt = 0
abi = 0
cdi = len(cd)-1
# ab는 앞에서 cd는 뒤에서부터 탐색
while abi<len(ab) and cdi>=0:
    if ab[abi] + cd[cdi] == 0: # 두개의 합이 0이면 개수 세아리기
        cnta = 0
        cntb = 0
        i = abi
        while abi < len(ab) and ab[i]== ab[abi]: # 같은게 있으면 인덱스 +1, 개수 세아리기
            abi += 1
            cnta += 1
        i = cdi
        while cdi >=0 and cd[i] == cd[cdi]: # 같은게 있으면 인덱스 +1, 개수 세아리기
            cdi -= 1
            cntb += 1
        cnt += cnta*cntb # 곱해서 카운트에 더하기
    elif ab[abi] + cd[cdi] < 0:
        abi += 1
    else:
        cdi -= 1

print(cnt)