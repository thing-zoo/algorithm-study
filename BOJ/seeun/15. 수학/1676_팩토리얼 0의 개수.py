n = int(input())

fact = 1
# 팩토리얼 구하기
for i in range(1, n+1):
    fact *= i

# 리스트로 변경
fact = list(str(fact))
cnt = 0

# 뒤에서부터 0 개수 카운튼
for i in range(len(fact)-1, -1, -1):
    if fact[i] == '0':
        cnt += 1
    else:
        break
print(cnt)