from collections import defaultdict
n, d, k, c = map(int, input().split())
sushi = [int(input()) for _ in range(n)]

cnt = 1
choose = defaultdict(int)
maxcnt = 0
choose[c] = 1

# 처음에 첫번째 초밥부터 k개를 먹음
for i in range(k):
    if choose[sushi[i]] == 0:
        cnt += 1
    choose[sushi[i]] += 1
maxcnt = cnt

# 양쪽 포인터를 오른쪽으로 옮겨가면서 확인
for l in range(n):
    r = (l+k)%n
    choose[sushi[l]] -=1 # 오른쪽으로 갈거니까 현재 왼쪽포인터는 안먹음 처리
    if choose[sushi[l]] == 0: # 만약에 하나도 안먹은 상태가 된다면 종류 -1
        cnt -=1
    if choose[sushi[r]] == 0: # 만약에 다음에 먹을 오른쪽 포인터 스시가 한번도 안먹은 스시라면 +1
        cnt += 1
    choose[sushi[r]] += 1 # 스시 먹음 표시
    maxcnt = max(maxcnt, cnt)
print(maxcnt)
