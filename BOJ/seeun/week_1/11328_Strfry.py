def check(a, b):
    a = list(a)
    b = list(b)
    a.sort()
    b.sort()
    if a == b:
        return True
    else:
        return False
    # if len(a)!=len(b):
    #     return False
    # elif a == b:
    #     return True
    # else:
    #     for i in range(len(a)):f
    #         if a[i] not in b:
    #             return False
    #     return True

n = int(input())
for i in range(n):
    a, b = input().split()
    if check(a, b) == True:
        print("Possible")
    else:
        print("Impossible")
