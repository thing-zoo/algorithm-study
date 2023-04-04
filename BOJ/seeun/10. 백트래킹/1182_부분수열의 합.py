N, S = map(int, input().split())
nums = list(map(int, input().split()))
tmp = []
arr = []
res = []

visited = [False]*N
cnt = 0

nums.sort()
def btk(num):
    global res, cnt
    if len(arr) >0 and sum(arr) == S: # 합이 S이고 비어있는 수열이 아니면
        cnt += 1
        # return

    for i in range(num, len(nums)): # nums 안에서 숫자고르기, 중복수열 안되기 때문에 시작점 지정
        if not visited[i]: # not in 대신 visit으로 체크: 똑같은 숫자가 들어갈 수 있지만 not in으로 하면 못들어감
            visited[i] = True
            arr.append(nums[i])
            btk(i+1)
            arr.pop()
            visited[i] = False
      
btk(0)
print(cnt)