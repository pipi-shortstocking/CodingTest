from collections import deque
import math


def solution(progresses, speeds):
    answer = []
    days = deque([math.ceil((100 - p) / s) for p, s in zip(progresses, speeds)])

    while days:
        base = days.popleft()
        cnt = 1
        
        while days and days[0] <= base:
            cnt += 1
            days.popleft()

        answer.append(cnt)

    return answer


progresses = [93, 30, 55]   
speeds = [1, 30, 5]
# [2, 1]
print(solution(progresses, speeds))
print()

progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]
# [1, 3, 2]
print(solution(progresses, speeds))