import sys

input = sys.stdin.readline


def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


t = int(input())

for _ in range(t):
    arr = list(map(int, input().split()))
    sum = 0

    # 조합 라이브러리를 사용하지 않아도 메모리와 시간은 동일함
    for i in range(1, len(arr)):
        for j in range(i + 1, len(arr)):
            sum += gcd(arr[i], arr[j])

    print(sum)
