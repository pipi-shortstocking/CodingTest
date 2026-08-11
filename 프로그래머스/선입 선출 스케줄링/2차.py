def solution(n, cores):
    if n <= len(cores):
        return n

    n -= len(cores)
    left = 1
    right = max(cores) * n

    while left <= right:
        mid = (left + right) // 2
        task = sum(mid // t for t in cores)

        if task >= n:
            right = mid - 1
        elif task < n:
            left = mid + 1

    time = left
    remain_task = n - sum((time - 1) // c for c in cores)

    for i, c in enumerate(cores):
        if time % c == 0:
            remain_task -= 1
            if remain_task == 0:
                return i + 1


n = 6
cores = [1,2,3]
print(solution(n, cores))