def star(n):
    if n == 1:
        return ['*']
    
    stars = star(n//3)
    tmp = []

    for s in stars:
        tmp.append(s*3)
    for s in stars:
        tmp.append(s+" "*(n//3)+s)
    for s in stars:
        tmp.append(s*3)

    return tmp

num = int(input())

cnt = 1

print("\n".join(star(num)))