def solution(n, cores):
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
    sorted_cores = sorted(cores)
    total_tasks = n

    for c in sorted_cores:
        finish_task = time // c
        
        if total_tasks > 0 :
            total_tasks -= finish_task

        if total_tasks <= 0:
            return cores.index(c) + 1


n = 6
cores = [1,2,3]
print(solution(n, cores))