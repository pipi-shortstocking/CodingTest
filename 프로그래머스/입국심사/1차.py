def solution(n, times):
    times.sort()
    
    def can_process(T):
        total = 0

        for time in times:
            total += T // time

        return total >= n # True는 시간을 더 줄일 수 있음, False는 시간을 더 늘려야 함
    
    start = 0
    end = times[-1] * n

    while start <= end:
        mid = (start + end) // 2

        if can_process(mid):
            end = mid - 1
        else:
            start = mid + 1

    return start # start가 end + 1값이 되면 최초로 가능한 시간 도출

n = 6
times = [7, 10]

print(solution(n, times))