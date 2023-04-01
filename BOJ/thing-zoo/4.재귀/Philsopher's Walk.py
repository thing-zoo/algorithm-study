def walk(n, m):
    if n == 2:
        if m == 0:
            return (1,1)
        elif m == 1:
            return (1,2)
        elif m == 2:
            return (2,2)
        else:
            return (2,1)
    
    half = n//2
    b = m//(half**2)
    if b == 0: 
        x, y = walk(half, m%(half**2))
        return (y, x)
    elif b == 1:
        x, y = walk(half, m%(half**2))
        return (x, y+half)
    elif b == 2: 
        x, y = walk(half, m%(half**2))
        return (x+half, y+half)
    else: 
        x, y = walk(half, m%(half**2))
        return (2*half-y+1, half-x+1)

n, m = map(int, input().split())
print(*walk(n, m-1))
