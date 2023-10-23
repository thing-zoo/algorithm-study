def solution(genres, plays):
    answer = []
    dic = {} # 장르별 플레이수, 고유번호 저장
    count = {} # 장르별 총 플레이수 계산
    for i in range(len(plays)):
        g = genres[i]
        p = plays[i]
        if g in dic.keys():
            dic[g].append([p, i]) # [플레이수, 고유번호] 형태로 저장
            count[g] += p
        else:
            dic[g] = [[p, i]]
            count[g] = p
            
    rank = sorted(list(count.items()), key=lambda x:-x[1]) # 총 플레이수가 많은 장르 순서대로 정렬
    for g, p in rank: # 총 플레이 수 많은 장르부터
        tmp = dic[g]
        tmp.sort(key=lambda x:(-x[0], x[1])) # 장르 내에서 플레이수 많은 순, 고유번호 낮은 순으로 정렬
        for i in range(min(len(tmp), 2)): # 최대 2개 선택
            answer.append(tmp[i][1])
    return answer