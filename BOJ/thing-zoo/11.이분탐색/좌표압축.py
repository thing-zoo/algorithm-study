import bisect
n = int(input())
x = list(map(int, input().split()))
x2 = sorted(set(x)) # 중복제거 후 정렬
for i in x:
    # i를 삽입할 가장 왼쪽 인덱스 찾기 == i보다 작은 요소 개수
    print(bisect.bisect_left(x2, i), end=' ')