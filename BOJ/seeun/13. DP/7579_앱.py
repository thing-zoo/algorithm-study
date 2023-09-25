import sys
input = sys.stdin.readline
n, m = map(int, input().split())
a, c = [0], [0]
a.extend(list(map(int, input().split())))
c.extend(list(map(int, input().split())))
empty = [[0]*(sum(c)+1) for _ in range(n+1)]
# empty[i][j] = i번째 앱이 종료될수있을때 j만큼의 에너지를 쓸 수 있음 => 그렇게 했을 때 최대로 확보할 수 있는 메모리
ans = sum(c)
for i in range(1, n+1): # i번째 앱을 종료할때
    for j in range(1, sum(c) + 1): # j만큼 에너지를 쓸 수있을 때
        if j >= c[i]: # i를 비활할 수 있는 에너지가 있다면
            empty[i][j] = max(empty[i-1][j], a[i] + empty[i-1][j-c[i]]) # i메모리 + i를 비활하고 남은 에너지로 얻을 수 있는 메모리
        else: # i를 비활할 수 없으면 이전 값 그대로
            empty[i][j] = empty[i-1][j]

        if empty[i][j] >= m:
            ans = min(j, ans)
print(ans if m != 0 else 0)