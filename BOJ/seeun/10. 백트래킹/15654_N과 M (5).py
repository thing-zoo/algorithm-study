n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
arr = [] # 길이 M인 수열 저장하는 배열

# visited 체크 대신 arr에 어팬드 팝
def btk(num):
    if len(arr) == m: # M개의 숫자 다 골랐으면 출력
        for i in arr:
            print(i, end=" ")
        print()
        return

    for i in range(len(nums)): # nums 안에서 숫자고르기
        if nums[i] not in arr:
            arr.append(nums[i])
            btk(i+1)
            arr.pop()

btk(1)