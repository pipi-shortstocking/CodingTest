def square(n, r, c):
    if n == 0:
        return 0

    half = 2 ** (n - 1)  # 한 변 길이의 절반

    # half를 기준으로 사분면
    if r < half and c < half:
        return square(n - 1, r, c)
    if r < half and c >= half:
        return half * half + square(n - 1, r, c - half)
    if r >= half and c < half:
        return 2 * half * half + square(n - 1, r - half, c)
    if r >= half and c >= half:
        return 3 * half * half + square(n - 1, r - half, c - half)


n, r, c = map(int, input().split())

print(square(n, r, c))
