import math
h, w, n, m = map(int, input().split())
garo = math.ceil(h/(n+1))
sero = math.ceil(w/(m+1))
print((garo)*(sero))