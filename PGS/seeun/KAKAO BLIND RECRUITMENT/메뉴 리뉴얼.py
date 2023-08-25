from itertools import combinations
from collections import Counter

def solution(orders, course):
    ans = []
    answer = []

    for c in course: # n개의 요리가 포함된 코스
        combi = []
        for o in orders: # 주문들 중에서 n개의 메뉴 조합 구하기
            o = sorted(o)
            if len(o)>= c:
                combi += combinations(o, c)
        cnt = Counter(combi) # 모든 주문들에서 조합들 개수 구하기
        if not cnt: # 조합이 없으면 패스
            continue

        maxcnt = max(cnt.values()) # 현재 코스에서 가장 많이 나온 조합의 개수
        if maxcnt == 1: # 두 팀 이상에서 주문되어야 됨
            continue
        for c in cnt.keys(): 
            if cnt[c] == maxcnt:
                answer.append(c)
            # elif cnt[c] < maxcnt:
            #     break
    for a in answer:
        ans.append("".join(a))
    ans.sort()
    return ans

print(solution(["XYZ", "XWY", "WXA"],	[2,3,4]))