n = int(input())
isused1 = [0 for _ in range(n)]
isused2 = [0 for _ in range(2 * n)]
isused3 = [0 for _ in range(2 * n)]
cnt = 0


def func(cur):
    global cnt

    if cur == n:
        cnt += 1
        return

    for i in range(n):
        if isused1[i] or isused2[cur + i] or isused3[cur - i + n - 1]:
            continue
        isused1[i] = 1
        isused2[cur + i] = 1
        isused3[cur - i + n - 1] = 1
        func(cur + 1)
        isused1[i] = 0
        isused2[cur + i] = 0
        isused3[cur - i + n - 1] = 0


func(0)
print(cnt)
