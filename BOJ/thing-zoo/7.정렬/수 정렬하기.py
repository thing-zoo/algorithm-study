def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
n = int(input())
arr = [ int(input()) for _ in range(n) ]
bubble_sort(arr)
for i in arr:
    print(i)