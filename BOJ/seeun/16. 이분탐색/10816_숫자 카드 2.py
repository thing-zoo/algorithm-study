
N = int(input())
arr_n = list(map(int,input().split()))
M = int(input())
arr_m = list(map(int,input().split()))

dic = dict()

# 몇개 있는지 카운트
for i in arr_n:
    try :
        dic[i] += 1
    except:
        dic[i] = 1

# 프린트
for i in arr_m:
    try:
        print(dic[i] , end = " ")
    except:
        print(0, end=" ")