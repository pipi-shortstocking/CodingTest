import sys

input = sys.stdin.readline

# 에라토스테네스의 체
n = 1000000
arr = [True] * (n + 1)

for i in range(2, int(n**0.5) + 1):
    if arr[i]:
        for j in range(i * 2, n, i):
            if arr[i]:
                arr[j] = False

while True:
    a = int(input())

    if a == 0:
        break

    for num in range(3, a - 2, 2):
        if arr[num] and arr[a - num]:
            print(a, "=", num, "+", a - num)
            break
    else:
        print('"Goldbach\'s conjecture is wrong."')
