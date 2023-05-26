import sys
input = sys.stdin.readline
n, d, k, c = map(int, input().strip().split())
sushi = [int(input()) for _ in range(n)]
answer = 0
# 시도 1: set 사용
# O(nk): python 시간초과 pypy 통과
# for start in range(n):
#     count = set() # 스시 종류 카운트
#     contain_c = False # c 포함 여부
#     for i in range(start, start + k): # 연속으로 k개 먹기
#         count.add(sushi[i%n])
#         if sushi[i] == c: contain_c = True # c도 먹었는지 확인

#     temp = len(count) # 먹은 스시 가짓수
#     if not contain_c: temp += 1 # c 안먹었다면 추가
#     answer = max(answer, temp) # 정답 갱신

# 시도 2: 구글링, 슬라이딩 윈도우 사용
from collections import defaultdict
count = defaultdict(int) # 스시 종류 카운트
count[c] += 1 # 미리 쿠폰 적용
# 초기 윈도우 카운트
for i in range(k):
    count[sushi[i]] += 1
end = k - 1
for start in range(n):
    answer = max(answer, len(count)) # 정답 갱신
    # 윈도우 슬라이드해주기
    count[sushi[start]] -= 1
    if count[sushi[start]] == 0: # 남은게 없다면
        count.pop(sushi[start]) # 삭제
    end = (end + 1)%n # end 한칸 이동
    count[sushi[end]] += 1 # 카운트

print(answer)