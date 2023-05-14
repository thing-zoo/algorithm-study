from itertools import combinations
n = int(input())

if n<10:
    print(n)
elif n>1022:
    print(-1)
else:
    ans = []
    for i in range(1, 11): # 자릿수
        for nums in combinations(range(10), i): # i자릿수 조합 생성
            tmp = sorted(list(nums), reverse=True) # 내림차순 정렬
            ans.append(int("".join(map(str, tmp)))) # 정수로 변경후 배열에 추가

    ans.sort() # 오름차순 정렬
    print(ans[n])
        