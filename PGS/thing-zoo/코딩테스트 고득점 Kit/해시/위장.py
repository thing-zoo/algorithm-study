def solution(clothes):
    answer = 1
    d = {}
    # d[종류] = [옷]
    for name, type in clothes:
        if type not in d:
            d[type] = [name]
        else:
            d[type].append(name)
    if len(d) > 1: #종류가 둘이상이면
        for k in d:
            answer *= len(d[k])+1 #(옷수+1)곱하고
        answer -= 1 #아무것도 안입는 경우 제외
    else: #종류가 하나면
        for k in d:
            answer *= len(d[k]) #옷 수

    return answer
clothes = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]
print(solution(clothes))