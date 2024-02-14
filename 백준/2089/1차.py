import sys

input = sys.stdin.readline

n = int(input())
ans = ""

if n == 0:
    print(0)
    exit()

while n:
    if n % -2:  # 딱 나눠 떨어지지 않는다면
        ans += "1"
        n = n // (-2) + 1
    else:
        ans += "0"
        n = n // (-2)
    # print(n, ans[::-1])

print(ans[::-1])
