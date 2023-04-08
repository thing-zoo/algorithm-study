n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

res = []
arr = [] # 길이 M인 수열 저장하는 배열
visited = [False] * n

def btk(num):
    global res
    if len(arr) == m: # M개의 숫자 다 골랐으면 출력
        tmp = arr[:] # arr를 append 하게 되면 주소 복사로 인해 빈 수열만 들어가게 됨.
        tmp = tuple(tmp) # set()은 문자열, 숫자, 튜플만 가능함.
        res.append(tmp)  
        return

    for i in range(len(nums)): # nums 안에서 숫자고르기
        if not visited[i]: # not in 대신 visit으로 체크: 똑같은 숫자가 들어갈 수 있지만 not in으로 하면 못들어감
            visited[i] = True
            arr.append(nums[i])
            btk(i+1)
            arr.pop()
            visited[i] = False

btk(1)
setres = set(res) # set으로 중복 제거
res = list(setres) # 리스트로 변경후 정렬
res.sort()
for i in range(len(res)):
    print(" ".join(map(str, res[i])))