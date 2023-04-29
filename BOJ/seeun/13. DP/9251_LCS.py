a = list(input())
b = list(input())
# ACAYKP
# CAPCAK
if len(a)<len(b):
    a, b = b, a
d = [0]*min(len(a), len(b))
for i in range(len(a)):
    cnt = 0
    for j in range(len(b)):
        if cnt < d[j]:
            cnt = d[j]
        elif a[i] == b[j]:
            d[j] = cnt +1

print(max(d))