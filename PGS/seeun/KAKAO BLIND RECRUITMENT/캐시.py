from collections import deque
def solution(cacheSize, cities):
    answer = 0
    # cache = PriorityQueue(cacheSize)
    cache = []
    isExist = {}
    time = 0
    # p = 0
    if cacheSize == 0:
        return len(cities*5)
    # for c in cities:
    #     # print(isExist)
    #     c = str(c).upper()
    #     heapq.heapify(cache)
    #     print(cache)
    #     if c in isExist.keys() and isExist[c]: # 도시가 캐시 안에 들어온적 있고 현재 캐시 안에 남아있으면
    #         print('hit', c)
    #         if len(cache) == cacheSize: # 힛인데 가득찼으면 우선순위 변경해줘야함
    #             for i in range(len(cache)):
    #                 if cache[i][1] == c:
    #                     cache[i][0] = p
    #             # isExist[cache.get()[1]] = False
    #         # cache.put((p, c))
    #         else:
    #             heapq.heappush(cache, [p, c]) # 힛인데 가득 안찻으면 그냥 넣으면 됨
    #         time += 1
    #     elif c in isExist.keys() and not isExist[c]: # 캐시에 들어온 적은 있지만 현재 캐시에는 없을 때
    #         print('miss', c)
    #         if len(cache) == cacheSize: # 만약 가득 찼다면 
    #             # isExist[cache.get()[1]] = False # 우선순위가 가장 낮은것 빼내기
    #             isExist[heapq.heappop(cache)[1]] = False 
                
    #         # cache.put((p, c))
    #         heapq.heappush(cache, [p, c])
    #         time += 5
    #     elif c not in isExist.keys(): # 한번도 들어온적 없는 도시이면 캐시안에는 당연히 없음
    #         print('miss', c)
    #         if len(cache) == cacheSize: # 만약 가득 찼다면 
    #             isExist[heapq.heappop(cache)[1]] = False 
    #         # cache.put((p, c))
    #         heapq.heappush(cache, [p, c])
    #         time += 5
    #     p += 1
    #     isExist[c] = True

    queue = deque(maxlen=cacheSize)
    for c in cities:
        c = str(c).upper()
        print(queue)
        if c not in queue: # miss 이면 그냥 넣기
            # print('miss', c)
            time += 5
            queue.append(c)
        else: # hit이면 
            # print('hit', c)
            queue.remove(c) # 원래 들어있던 값을 지우고
            queue.append(c) # 새롭게 뒤에다가 추가
        
            time += 1
    answer = time
    return answer

cacheSize, cities =  3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
print(solution(cacheSize, cities))