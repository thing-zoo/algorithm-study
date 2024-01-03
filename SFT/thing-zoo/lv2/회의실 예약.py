n, m = map(int, input().split())
rooms = {}
for _ in range(n):
  r = input()
  rooms[r] = [False]*18 + [True]
for _ in range(m):
  r, s, t = input().split()
  for i in range(int(s), int(t)):
    rooms[r][i] = True
    
result = sorted(rooms.keys())
for i in range(len(result)):
  r = result[i]
  print('Room %s:' %r)
  times = []
  s = 0
  for j in range(9, 19):
    if s == 0 and not rooms[r][j]:
      s = j
    elif s != 0 and rooms[r][j]:
      times.append((s, j))
      s = 0
  if not times:
    print('Not available')
  else:
    print('%d available:' %len(times))
    for s, t in times:
      print('%02d-%02d' %(s, t))
  if i != (len(result) - 1): print('-----')
