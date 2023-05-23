def find_start(arr, k): # k가 시작되는 위치 찾는 함수
    start = 0
    end = len(arr)
    while start < end:
        mid = (start+end)//2
        if arr[mid] < k: start = mid + 1
        else: end = mid
    return start
def find_end(arr, k): # k가 끝나는 다음 위치 찾는 함수
    start = 0
    end = len(arr)
    while start < end:
        mid = (start+end)//2
        if arr[mid] <= k: start = mid + 1
        else: end = mid
    return end
n = int(input())
a = sorted(list(map(int, input().split())))
m = int(input())
for i in list(map(int, input().split())):
    # import bisect 라이브러리도 있음
    start = find_start(a, i) # bisect.bisect_left(a, i)
    end = find_end(a, i) # bisect.bisect(a, i)
    print(end - start, end=" ")