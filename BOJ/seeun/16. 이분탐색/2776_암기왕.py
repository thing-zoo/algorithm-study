import sys
def input():
    return sys.stdin.readline()

def binsearch(length, num):
    s = 0
    e = length-1
    while s <= e:
        mid = (s+e)//2
        if nums1[mid] == num:
            return True
        if nums1[mid] < num:
            s = mid+1
        else:
            e = mid-1
    return False

t = int(input())
for _ in range(t):
    n = int(input())
    nums1 = list(map(int, input().split()))
    nums1.sort()
    m = int(input())
    nums2 = list(map(int, input().split()))
    for n2 in nums2:
        if binsearch(n, n2):
            print(1)
        else:
            print(0)