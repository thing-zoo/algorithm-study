from itertools import combinations
n = int(input())
arr = []
for i in range(1,11): # 1자리수부터~10자리수까지
    for (selected) in combinations(range(10), i): # 0~9로 길이 i인 수의 조합구하기
        selected = list(selected)
        selected.sort(reverse=True) # 각 자릿수를 내림차순 정렬
        arr.append(int("".join(map(str, selected))))
arr.sort() # 전체 수는 오름차순 정렬

if n < len(arr):
    print(arr[n])
else:
    print(-1)