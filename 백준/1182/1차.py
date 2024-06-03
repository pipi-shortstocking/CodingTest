n, s = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0


def func(cur, total):
    global cnt

    if cur == n:  # cur이 끝을 가리키고
        if total == s:  # 전체 합이 s일 때
            cnt += 1
        return

    # 현재 cur이 가리키는 값을 더하지 않을 때
    func(cur + 1, total)

    # 현재 cur이 가리키는 값을 더할 때
    func(cur + 1, total + arr[cur])


func(0, 0)
if s == 0:
    cnt -= 1  # 공집합 삭제
print(cnt)
