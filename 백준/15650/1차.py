n, m = map(int, input().split())

arr = [0 for _ in range(10)]
isused = [False for _ in range(10)]


def func(cur, start):
    if cur == m:
        for idx in range(m):
            if arr[idx] == 0:
                return
            print(arr[idx], end=" ")
        print()
        return

    for i in range(start, n + 1):
        if not isused[i]:
            arr[cur] = i
            isused[i] = True
            func(cur + 1, i)  # 현재 어떤 숫자까지 썼는지 전달
            isused[i] = False


func(0, 0)
