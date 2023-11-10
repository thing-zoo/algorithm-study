from collections import deque
def solution(cacheSize, cities):
    answer = 0
    cache = deque() #maxlen이라는게 있다고함...!!
    for city in cities:
        city = city.lower()
        if city in cache:
            cache.remove(city)
            cache.append(city)
            answer += 1
        else:
            while cache and len(cache) >= cacheSize:
                cache.popleft()
            if cacheSize > 0:
                cache.append(city)
            answer += 5
    return answer