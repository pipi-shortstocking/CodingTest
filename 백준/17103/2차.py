import sys, math, itertools

input = sys.stdin.readline


def pri(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


t = int(input())

for _ in range(t):
    n = int(input())
    cnt = 0

    pri_arr = [i for i in range(2, n) if pri(i)]

    if int(n / 2) in pri_arr:
        cnt += 1

    result = list(itertools.combinations(pri_arr, 2))

    for j in range(len(result)):
        if sum(result[j]) == n:
            cnt += 1
    print(cnt)
