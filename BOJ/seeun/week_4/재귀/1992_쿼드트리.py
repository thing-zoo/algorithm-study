res = []
def check(i, j, n):
    global res

    first = maps[i][j]
    for p in range(i, i+n):
        for q in range(j, j+n):
            if maps[p][q] != first:
                res.append("(") # 한뭉치 시작할 때마다 괄호열기
                check(i, j, n//2)
                check(i, j+n//2, n//2)
                check(i+n//2, j, n//2)
                check(i+n//2, j+n//2, n//2)
                res.append(")") # 뭉치 끝나면 괄호 닫기
                return

    res.append(str(first))

n = int(input())
maps = []

for i in range(n):
    tmp = list(input())
    tmplist = list(map(int, tmp))
    maps.append(tmplist)

check(0, 0, n)
print(*res, sep="")