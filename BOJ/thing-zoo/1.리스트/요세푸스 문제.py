n, k = map(int, input().split())
data = [ i for i in range(1, n+1) ]

i = 0
size = n
print('<', end='')
while data:
    i = (i+k-1)%size
    tmp = data[i]
    if len(data) == 1:
        print(tmp, end='>')
    else:
        print(tmp, end=', ')
    data.remove(tmp)
    size -= 1