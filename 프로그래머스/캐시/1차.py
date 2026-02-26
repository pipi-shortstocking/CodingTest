from collections import deque

def solution(cacheSize, cities):
    if cacheSize < 1:
        return len(cities) * 5

    time = 0
    cache = deque(maxlen = cacheSize) # 캐시 설정

    for city in cities:
        nor_city = city.lower()

        if nor_city not in cache: # miss
            time += 5
            if len(cache) >= cacheSize:
                cache.popleft() # 오래된 캐시 삭제
            cache.append(nor_city) # 캐시 저장

        elif nor_city in cache: # hit
            time += 1
            cache.remove(nor_city) # hit 캐시 삭제
            cache.append(nor_city) # 최근 캐시로 조정

    return time


# cacheSize = 3
# cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]

# cacheSize = 3
# cities = ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]

# cacheSize = 2
# cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]

# cacheSize = 5
# cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]

# cacheSize = 2
# cities = ["Jeju", "Pangyo", "NewYork", "newyork"]

cacheSize = 0
cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]

print(solution(cacheSize, cities))