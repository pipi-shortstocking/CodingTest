n, m = map(int, input().split())

arr = [0 for _ in range(10)]


def func(k):
    if k == m:
        for idx in range(n):
            if arr[idx] == 0:
                break
            print(arr[idx], end=" ")
            if idx == m - 1:
                print()
        return

    for i in range(arr[k - 1], n + 1):
        arr[k] = i
        func(k + 1)


func(0)
