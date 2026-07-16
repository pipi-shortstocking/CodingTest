def solution(distance, rocks, n):
    rocks.sort()
    rocks.append(distance)
    left, right = 0, rocks[-1]

    while left <= right:
        mid = (left + right) // 2
        current = 0
        cnt = 0

        for rock in rocks:
            dist = rock - current

            if dist < mid:
                cnt += 1

                if cnt > n:
                    break
            else:
                current = rock

        if cnt > n: # n 이상으로 바위를 제거했으면 간격 줄이기
            right = mid - 1
        else:
            answer = mid
            left = mid + 1
    
    return answer

distance = 25
rocks = [2, 14, 11, 21, 17]
n = 2
print(solution(distance, rocks, n))