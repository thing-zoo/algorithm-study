def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    print(*arr)

def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    print(*arr)

def merge_sort(arr):
    if len(arr) == 1:
        return arr
    
    # 분할
    mid = len(arr)//2
    left_arr = merge_sort(arr[:mid])
    right_arr = merge_sort(arr[mid:])

    # 합병
    merged = []
    l = r = 0
    while l < len(left_arr) and r < len(right_arr): # 두 배열을 비교해서 넣고
        if left_arr[l] < right_arr[r]: 
            merged.append(left_arr[l])
            l += 1
        else:
            merged.append(right_arr[r])
            r += 1
    merged += left_arr[l:]  # 남은 값 마저 넣어주기
    merged += right_arr[r:]

    return merged

def quick_sort(arr, start, end):
    if start + 1 >= end: return
    pivot = start
    l = start + 1; r = end - 1
    while True:
        while l <= r and arr[pivot] > arr[l]: l += 1
        while l <= r and arr[pivot] <= arr[r]: r -= 1
        if l > r: break
        arr[l], arr[r] = arr[r], arr[l]
    arr[pivot], arr[r] = arr[r], arr[pivot]
    quick_sort(arr, start, r)
    quick_sort(arr, r+1, end)

def counting_sort(arr):
    count = [0] * (max(arr) + 1) #인덱스가 0~max인 배열

    # 각 값 카운팅
    for num in arr:
        count[num] += 1
    
    # 해당 값의 마지막 인덱스 구하기
    for i in range(len(count)-1):
        count[i+1] += count[i]
    
    # 정렬된 결과 넣기
    result = [0] * (len(arr))
    for num in arr:
        i = count[num]
        result[i - 1] = num
        count[num] -= 1
    print(*result)

from collections import deque
def radix_sort(arr):
    buckets = [deque() for _ in range(10)]

    max_val = max(arr)  # 최대값이 가진 자릿수까지 돌려야함
    cur_ten = 1         # 일의 자리부터시작
    q = deque(arr)

    while max_val >= cur_ten:
        while q:
            x = q.popleft()
            buckets[(x // cur_ten) % 10].append(x)
        for bucket in buckets:
            while bucket:
                q.append(bucket.popleft())
        cur_ten *= 10
    return list(q)

arr = [3, 2, 7, 116, 62, 235, 1, 23, 55, 77]
# counting_sort([4, 7, 9, 1, 3, 5, 2, 3, 4])
print(radix_sort([15, 27, 64, 25, 50, 17, 39, 28]))