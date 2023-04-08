n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

res = []
arr = [] # 길이 M인 수열 저장하는 배열

def btk():
    global res
    if len(arr) == m: # M개의 숫자 다 골랐으면 출력
        tmp = arr[:] # arr를 append 하게 되면 주소 복사로 인해 빈 수열만 들어가게 됨.
        tmp = tuple(tmp)
        res.append(tmp)  
        return

    for i in range(len(nums)): # 중복체크 안해도 됨, 숫자 범위 필요없음.
        arr.append(nums[i])
        btk()
        arr.pop()
      
btk()
setres = set(res) # set으로 중복 제거
res = list(setres) # 리스트로 변경후 정렬
res.sort()
for i in range(len(res)):
    print(" ".join(map(str, res[i])))