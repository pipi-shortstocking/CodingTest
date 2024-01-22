import sys

input = sys.stdin.readline
num = 0

while True:
    l, p, v = map(int, input().split())
    num += 1

    if l == 0 and p == 0 and v == 0:
        break

    ans = (v // p) * l + (v % p)

    print("Case " + str(num) + ": " + str(ans))
