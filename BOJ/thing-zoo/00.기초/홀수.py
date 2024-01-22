result = []
for i in range(7):
    data = int(input())
    if data%2 != 0:
       result.append(data)

if not result : #emtpy->T
    print(-1)
else:
    print(sum(result))
    print(min(result))