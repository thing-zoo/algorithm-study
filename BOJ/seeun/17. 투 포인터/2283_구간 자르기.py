n, k = map(int, input().split())
line = [0]*1000001 # 현재 지점에 몇개의 구간이 포함되어있는지 카운트
minl, maxr = 1000001, -1 # 여러 구간들의 제일 왼쪽점과 오른쪽점

for i in range(n):
    a, b = map(int, input().split())
    line[a] += 1 # 이 지점부터 라인 하나 시작함
    line[b] -= 1 # 이 지점에서 끝남 -> 라인하나 빼줌
    minl = min(minl, a)
    maxr = max(maxr, b)

for i in range(minl+1, maxr+1): # i에 몇개의 라인이 있는지 정리
    line[i] += line[i-1]

r = minl
total = 0
for l in range(maxr): # 왼쪽 포인터를 오른쪽으로 옮겨가면서 탐색
    # k를 처음 넘는 구간을 구함
    while r<maxr and total < k: 
        total += line[r]
        r += 1
    
    # 종료조건 - k를 만들었거나 r이 끝까지 갔으면
    if total == k:
        break
    if r == maxr:
        break

    # l을 옮기기 전에 누적합에서 빼주기
    total -= line[l]

if total == k: # k를 만나서 끝난거면 - 정답출력
    print(l, r)
else: # 아니면 0 출력
    print(0, 0)