def solution(n, times):
    times = sorted(times)
    mid = sum(times) // len(times) * n
    judge = len(times)
    start = 0
    end = times[-1] * n
    
    while True:
        people = 0 # mid 시간 동안 처리 가능한 인원

        for t in times:
            people += mid // t

        if people == n:
            return mid

        if people < n:
            start = mid
        elif people > n:
            end = mid
        
        mid = (start + end) // judge



n = 6
times = [7, 10]
print(solution(n, times))