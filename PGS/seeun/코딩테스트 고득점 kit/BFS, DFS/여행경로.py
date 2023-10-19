ans = []

def solution(tickets):
    arr = []
    used = [False] * len(tickets)
    dfs(tickets, "ICN", used, arr)
    ans.sort() # 알파벳 순으로 앞서는 루트 차지 
    return ans[0]

def dfs(tickets, city, used, arr): # 백트래킹으로 루트 찾기
    
    # 사용안한 티켓이 없으면
    if used.count(False) == 0: 
        arr.append(city) # 마지막 도착 도시 까지 넣고
        ans.append(arr[:]) # 정답 배열에 저장
        arr.pop() # 마지막 도시 pop
        return
    
    for i in range(len(tickets)):
        t = tickets[i]
        if not used[i] and t[0] == city: # 해당 도시에서 출발하는 티켓이 있으면 & 아직 사용안했으면
            used[i] = True # 사용 표시
            arr.append(city) # 방문한 도시 배열에 넣기
        
            dfs(tickets, t[1], used, arr)
            
            used[i] = False # 사용 취소
            arr.pop() # 방문한 도시 배열에서 빼기

print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))