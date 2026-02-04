import sys
input = sys.stdin.readline

N, C = map(int, input().split())
houses = []

for _ in range(N):
    house = int(input())
    houses.append(house)

houses.sort()

def can_install(mid):
    last = houses[0] # 공유기를 마지막으로 설치한 위치
    cnt = 1

    for i in range(1, N):
        if houses[i] - last >= mid: # 기준 거리를 넘는 집에 설치하기 위함
            cnt += 1
            last = houses[i]

    return cnt >= C # 거리가 mid 일 때 설치한 공유기 수와 설치해야 하는 공유기 수 비교

start = 1
end = houses[-1] - houses[0]

while start <= end:
    mid = (start + end) // 2
    
    if can_install(mid): # 공유기 수가 같거나 많으면 거리를 늘려보기
        start = mid + 1
    else: # 공유기 수가 적으면 거리를 줄여보기
        end = mid - 1

print(end)