n = int(input())
blog = list(input())

r = 0 # 빨간색 구간 카운트
b = 0 # 파란색 구간 카운트
if blog[0] == 'B':
    b += 1
else:
    r += 1

# 색깔이 바뀌는 구간이 몇번 있는지 체크
for i in range(1, n):
    if blog[i] != blog[i-1]:
        if blog[i] == 'B':
            b += 1
        else:
            r += 1

# 색깔이 바뀔 때마다 바꿔가며 칠하기 VS 모두 한 색깔로 칠한 후 다른 색을 골라 칠하기
print(r+b if r+b < 1+min(r, b) else 1+min(r, b))