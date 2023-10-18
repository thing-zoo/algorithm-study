def solution(players, callings):
    answer = []
    rank = {}
    for i in range(len(players)):
        rank[players[i]] = i # 선수-등수

    for c in callings:
        i = rank[c] # i: c선수의 등수
        
        rank[c] = i-1 # 한 등수 올림
        rank[players[i-1]] = i # 한등수 내림
        players[i], players[i-1] = players[i-1], players[i] # 서로 바꿔줌
    
    
    return players