from itertools import combinations
t = int(input())

for _ in range(t):
    nums = list(map(int, input().split()))
    total = 0 # 이 테스트케이스의 정답 저장
    for a, b in combinations(nums[1:], 2): # 조햡: 숫자 두개 골라오기
        res = 1 # 이 조합의 최대공약수 저장
        i = 2
        while i<=min(a, b):
            if a % i == 0 and b % i == 0:
                a //= i
                b //= i
                res *= i
            else:
                i += 1
        total += res # 이 조합의 최대공약수 합하기
    print(total)
