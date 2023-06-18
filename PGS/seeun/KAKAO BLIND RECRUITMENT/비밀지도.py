def solution(n, arr1, arr2):
    answer = []
    map1 = []
    map2 = []
    
    for i in range(n):
        b1 = bin(arr1[i])[2:] # 앞에 0b가 추가되기 때문에 없애고 받아와야함
        b2 = bin(arr2[i])[2:]

        # 자릿수를 n으로 맞춰주기 위함
        if len(b1) < n+2:
            b1 = " "*(n-len(b1)) + b1
        if len(b2) < n+2:
            b2 = " "*(n-len(b2)) + b2
        map1.append(b1)
        map2.append(b2)
    
    # 두 지도를 합쳐서 하나의 지도로 만듦
    for i in range(n):
        tmp = []
        for j in range(n):
            if map1[i][j] == '1' or map2[i][j] == '1':
                tmp.append("#")
            else:
                tmp.append(" ")
        answer.append("".join(tmp))
    
    return answer