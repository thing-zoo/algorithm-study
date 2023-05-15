def my_sqrt(x):
    if x < 2: 
        return x
    
    start = 1
    end = x
    while start <= end:
        mid = (start+end)//2
        expect = mid ** 2
        if expect == x: # 완전제곱수라면
            return mid  # 반환
        elif expect > x: # 기대값이 더 크면
            end = mid - 1 # 왼쪽으로
            result = mid # 이전값 저장
        else: # 기대값이 더 작으면
            start = mid + 1 # 오른쪽으로
    return result # 완전제곱수가 아니면 탈출후 이전값 반환

n = int(input())
print(my_sqrt(n))