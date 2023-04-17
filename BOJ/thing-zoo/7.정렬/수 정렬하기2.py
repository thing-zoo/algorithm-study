def merge_sort(arr):
    if len(arr) == 1:
        return arr
    
    mid = len(arr)//2
    left_arr = merge_sort(arr[:mid])
    right_arr = merge_sort(arr[mid:])

    l = r = 0
    merged = []
    while l < len(left_arr) and r < len(right_arr):
        if left_arr[l] < right_arr[r]:
            merged.append(left_arr[l])
            l += 1
        else:
            merged.append(right_arr[r])
            r += 1
    merged += left_arr[l:]
    merged += right_arr[r:]

    return merged

n = int(input())
arr = [ int(input()) for _ in range(n) ]
arr = merge_sort(arr)
for i in arr:
    print(i)