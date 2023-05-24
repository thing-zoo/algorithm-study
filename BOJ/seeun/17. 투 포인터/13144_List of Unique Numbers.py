from collections import defaultdict

n = int(input())
nums = list(map(int, input().split()))

cnt = 0
j = 0
numdict = defaultdict(int)
for i in range(n):
    while j<n and numdict[nums[j]]<1: # 아직 방문하지 않은 숫자이고 j가 범위 내이면
        numdict[nums[j]]=1 # 방문처리
        j += 1 # 오른쪽으로 한 칸
    
    # j가 끝까지 갔거나 반복되는 숫자가 하나 나오면 멈춤
    cnt += (j-i) # j-i 종류의 수열을 만들 수 있음
    numdict[nums[i]]=0 # 방문처리 취소
print(cnt)