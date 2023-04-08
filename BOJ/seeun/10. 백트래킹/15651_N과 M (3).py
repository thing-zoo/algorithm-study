n, m = map(int, input().split())

arr = [] # 길이 M인 수열 저장하는 배열

# visited 체크 대신 arr에 어팬드 팝
def btk():
    if len(arr) == m: # M개의 숫자 다 골랐으면 출력
        for i in arr:
            print(i, end=" ")
        print()
        return

    for i in range(1, n+1): # 1~N까지의 수
        arr.append(i)
        btk()
        arr.pop()

btk() # 중복체크를 할 필요가 없기 때문에 인자 x