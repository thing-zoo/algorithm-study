n, m = map(int, input().split())
char = list(input().split())
char.sort()
mo_cnt = 0
ja_cnt = 0

arr = []
def dfs(start):
    global mo_cnt, ja_cnt
    if len(arr) == n and mo_cnt >= 1 and ja_cnt >= 2:
        print("".join(arr))
        return
    
    for i in range(start, m):
        if not arr:
            if char[i] in ['a','e', 'i', 'o', 'u']: # 모음이면 
                mo_cnt += 1
            else:
                ja_cnt += 1
            arr.append(char[i])
            dfs(i+1)
            arr.pop()
            if char[i] in ['a','e', 'i', 'o', 'u']: 
                mo_cnt -= 1
            else:
                ja_cnt -= 1
        elif ord(arr[-1]) < ord(char[i]):
            if char[i] in ['a','e', 'i', 'o', 'u']: # 모음이면 
                mo_cnt += 1
            else: # 자음이면
                ja_cnt += 1
            arr.append(char[i])
            dfs(i+1)
            arr.pop()
            if char[i] in ['a','e', 'i', 'o', 'u']: 
                mo_cnt -= 1
            else:
                ja_cnt -= 1


dfs(0)