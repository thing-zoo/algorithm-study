t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    team = []
    for i in range(1, 201): # 6명이 참가한 팀 고르기
        if nums.count(i) == 6:
            team.append(i)
    dic = {}
    rank = 1
    for i in range(n):
        if nums[i] in team: # 6명이 참가한 팀이면
            if nums[i] in dic.keys(): # 이미 딕셔너리에 있으면
                dic[nums[i]].append(rank)
            else: # 딕셔너리에 없으면
                dic[nums[i]] = [rank]
            rank += 1
    
    ans = []
    for k in dic.keys():
        ans.append([k, sum(list(dic[k])[:4]), dic[k][4]])

    ans.sort(key=lambda x:(x[1],x[2])) # 점수합, 5번째 선수 기준 오름차순으로 정렬
    print(ans[0][0])