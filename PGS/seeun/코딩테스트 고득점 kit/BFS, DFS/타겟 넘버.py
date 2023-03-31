numbers = [4, 1, 2, 1]
target = 4

cnt = 0

def dfs(num, i):
    global cnt
    
    if num == target and i == len(numbers)-1: # 타겟넘버랑 같고 모든 숫자 다 썼으면
        cnt += 1
        return
    else:
        i += 1
        if i==len(numbers): # 배열 범위 벗어나면
            return False
        dfs(num+numbers[i], i) # + 해보기
        dfs(num-numbers[i], i) # - 해보기

dfs(0, -1)
print(cnt)