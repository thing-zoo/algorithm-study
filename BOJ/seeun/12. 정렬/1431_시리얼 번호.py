n = int(input())
serial = []
for _ in range(n):
    serial.append(input())

# 글자 길이 기준으로 정렬
serial.sort(key=len)
tmp = {}

#숫자인글자의 합 구하기
for i in range(n):
    total = 0
    if str(serial[i]).isalnum(): #숫자, 문자 같이있는 문자열이면
        for j in range(len(serial[i])):
            string = str(serial[i][j])
            if string.isdecimal(): # 숫자들의 합을 더함
                total += int(string)
    tmp[serial[i]] = total

# 문자열에 포함된 숫자기준 -> 사전순
serial = dict(sorted(tmp.items(), key=lambda x:(x[1], x[0])))
# 위에서 정렬된 딕셔너리의 key 값만 가져와서 길이순으로 정렬
serial = sorted(serial.keys(), key=len)
for i in range(len(serial)):
    print(serial[i])