def check(a, b):
    a = list(a)
    b = list(b)
    a.sort()
    b.sort()
    if a == b:
        return True
    else:
        return False

n = int(input())
for i in range(n):
    a, b = input().split()
    if check(a, b) == True:
        print("Possible")
    else:
        print("Impossible")
