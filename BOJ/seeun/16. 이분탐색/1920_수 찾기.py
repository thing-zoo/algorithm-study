a_len = int(input())
a = list(map(int, input().split()))
b_len = int(input())
b = list(map(int, input().split()))

a.sort()

def binary_search(num, arr):
    start = 0
    end = len(arr)-1
    mid = (start+end)//2

    while start <= end:
        mid = (start+end)//2
        if arr[mid] == num:
            return mid
        elif arr[mid] < num:
            start = mid +1
        elif num < arr[mid]:
            end = mid -1
    return -1

for i in range(b_len):
    if binary_search(b[i], a)!= -1:
        print(1)
    else:
        print(0)
