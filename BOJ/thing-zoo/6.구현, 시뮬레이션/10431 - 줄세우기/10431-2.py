for _ in range(int(input())):
    arr = list(map(int, input().split()))
    count = 0
    for i in range(1, len(arr)-1): # n-1번만 돌면됨
        for j in range(i+1, len(arr)): # i 뒤의 모든 수에 대해
            if arr[i] > arr[j]: # i 보다 작으면
                arr[i], arr[j] = arr[j], arr[i] # 바꾸기
                count += 1 # 걸음수 세기
    print(arr[0], count, sep=' ')