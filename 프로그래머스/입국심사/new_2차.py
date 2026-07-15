def solution(n, times):
    times.sort()
    left = 1
    right = times[-1] * n

    while left <= right:
        mid = (left + right) // 2
        time = sum(mid // t for t in times)

        if time >= n: # 충분하지만 더 줄일 수 있다
            right = mid - 1
        elif time < n:
            left = mid + 1

    return left

n = 6
times = [7, 10]
print(solution(n, times))