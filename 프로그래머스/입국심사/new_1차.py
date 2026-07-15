def solution(n, times):
    times.sort()
    left = 1
    right = times[-1] * n

    while left <= right:
        mid = (left + right) // 2
        time = sum(mid // t for t in times)
    
        if time == n:
            return mid
        elif time < n:
            left = mid + 1
        else:
            right = mid - 1

n = 6
times = [7, 10]
print(solution(n, times))