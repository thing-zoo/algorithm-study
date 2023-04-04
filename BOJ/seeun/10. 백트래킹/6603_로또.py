n = list(map(int, input().split()))
nums = n[1:]
n = n[0]
while n != 0:
    arr = []
    def dfs(start):
        if len(arr) == 6:
            print(" ".join(map(str,arr)))
            return
        for i in range(start, len(nums)): # 중복 막기 위해 start 설정
            arr.append(nums[i])
            dfs(i+1)
            arr.pop()
    dfs(0)
    print()
    n = list(map(int, input().split()))
    nums = n[1:]
    n = n[0]