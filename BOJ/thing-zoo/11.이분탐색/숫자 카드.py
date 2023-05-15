def binary_search(arr, k):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end)//2
        if arr[mid] == k:
            return 1
        elif arr[mid] < k:
            start = mid + 1
        else:
            end = mid - 1
    return 0
n = int(input())
a = sorted(list(map(int, input().split())))
m = int(input())
for i in list(map(int, input().split())):
    print(binary_search(a, i), end=' ')