n = int(input())
data = input()
count = {'R':0, 'B':0} # 문자별 칠한 횟수
count[data[0]] += 1 # 처음 색 칠하기
for i in range(1, n):
    if data[i] != data[i-1]: # 다른 색이면
        count[data[i]] += 1 # 칠하는 횟수 더하기
answer = min(count['R'], count['B']) + 1 # 칠할 횟수가 더 많은것을 먼저 칠하고(+1) 나머지를 더한다(min)
print(answer)