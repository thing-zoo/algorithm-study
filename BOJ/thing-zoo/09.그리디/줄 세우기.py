# (n - 1씩 차이나는 오름차순의 길이)만큼 옮기면 됨
n = int(input())
children = list(map(int, input().split()))
idx = [-1]*(n+1)
for i, num in enumerate(children): # 오름차순 비교를 위해
    idx[num] = i # 각 숫자의 인덱스 저장
max_length = 0 # 1씩 차이나는 오름차순 최대 길이
length = 1
for i in range(1, n):
    if idx[i] < idx[i+1]: # 오름차순이면
        length += 1 # 길이 증가
    else: # 오름차순이 끊기면
        max_length = max(length, max_length) # 현재최대값과 비교
        length = 1 # 초기화
print(n - max_length if n != 1 else 0)