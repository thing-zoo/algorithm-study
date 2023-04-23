def check(num):
    global blist
    stt = 0
    end = len(blist)-1
    cnt = -1
    while stt<=end:
        mid = (stt+end)//2
        if num>blist[mid]:
            cnt = mid # num 보다 작은 것들의 개수 저장
            stt = mid+1
        else:
            end = mid-1
    return cnt

n = int(input())

for _ in range(n):
    res = 0
    an, bn = map(int, input().split())
    alist = list(map(int, input().split()))
    blist = list(map(int, input().split()))
    alist.sort()
    blist.sort()
    for i in range(len(alist)):
        res += check(alist[i])+1
    print(res)