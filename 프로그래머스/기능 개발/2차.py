def solution(progresses, speeds):
    import math
    from collections import deque

    extra = [100 - progress for progress in progresses]
    length = len(extra)
    days = deque([])

    for i in range(length):
        days.append(math.ceil(extra[i] / speeds[i]))

    # 위 계산 과정을 한 줄로 설정 가능
    # days = [math.ceil((100 - p) / s) for p, s in zip (progresses, speeds)]
    
    answer = []
    n = 1
    num = days.popleft()
    while days:
        if num < days[0]:
            answer.append(n)
            n = 1
            num = days.popleft()
        else:
            n += 1
            days.popleft()

        # # 혹은
        # if num >= days[0]: # 뒤 작업이 같이 끝날 경우도 고려해야 함(days[5, 5, 7, 3])
        #     n += 1
        #     days.popleft()
        # else:
        #     answer.append(n)
        #     n = 1
        #     num = days.popleft()

    answer.append(n)

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