n, m = map(int, input().split())

arr = [0 for _ in range(10)]


def func(k):
    if k == m:  # 자릿수 k가 m과 일치할 경우
        for idx in range(n):
            if arr[idx] == 0:
                break
            print(arr[idx], end=" ")
        print()
        return

    for i in range(1, n + 1):  # 중복 금지 조건 해제
        arr[k] = i
        func(k + 1)


func(0)
