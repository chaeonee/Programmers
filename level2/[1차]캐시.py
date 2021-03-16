from collections import deque

def solution(cacheSize, cities):
    answer = 0
    DB = deque()
    for city in cities:
        city = city.lower()
        if city in DB:
            answer += 1
            DB.remove(city)
            DB.append(city)
        else:
            answer += 5
            if cacheSize > 0:
                if len(DB) >= cacheSize and DB:
                    DB.popleft()
                DB.append(city)
    return answer
