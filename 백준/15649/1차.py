n, m = map(int, input().split())

arr = [0 for _ in range(10)]
isused = [False for _ in range(10)]


def func(k):
    if k == m:
        for idx in range(n):
            if arr[idx] == 0:
                break
            print(arr[idx], end=" ")
        print()
        return

    for i in range(1, n + 1):
        if not isused[i]:
            arr[k] = i
            isused[i] = True
            func(k + 1)
            isused[i] = False


func(0)
