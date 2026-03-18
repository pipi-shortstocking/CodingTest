def solution(n, times):
    times.sort()
    start = 0
    end = times[-1] * n

    def can_process(mid):
        people = 0

        for t in times:
            people += mid // t

        return people >= n # True는 시간을 더 줄일 수 있음 False는 이미 시간이 부족하므로 줄이기 불가

    while start <= end:
        mid = (start + end) // 2

        if can_process(mid):
            end = mid - 1
        else:
            start = mid + 1

    return start


n = 6
times = [7, 10]
print(solution(n, times))