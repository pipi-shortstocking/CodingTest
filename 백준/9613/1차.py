import sys, itertools

input = sys.stdin.readline


def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


t = int(input())

for _ in range(t):
    arr = list(map(int, input().split()))
    arr = arr[1:]
    sum = 0

    for i in itertools.combinations(arr, 2):
        sum += gcd(i[0], i[1])
        # math.gcd와 메모리의 차이만 있을 뿐, 시간 차이는 없음

    print(sum)
