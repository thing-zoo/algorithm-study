x, y = map(int, input().split())

def rev(n):
    rev_n = str(n)[::-1] # 뒤집어서
    return int(rev_n) # int로 변환후 리턴

x = rev(x)
y = rev(y)
print(rev(x+y))