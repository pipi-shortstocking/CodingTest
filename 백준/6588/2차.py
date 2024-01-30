import sys, math

input = sys.stdin.readline

# 에라토스테네스의 체
n = 1000000
arr = [True] * (n + 1)

for i in range(2, int(math.sqrt(n)) + 1):
    if arr[i]:
        j = 2
        while i * j <= n:
            arr[i * j] = False
            j += 1

while True:
    a = int(input())

    if a == 0:
        break

    for num in range(3, a - 3, 2):
        if arr[num] and arr[a - num]:
            print(str(a) + " = " + str(num) + " + " + str(a - num))
            break
    else:
        print("Goldbach's conjecture is wrong.")
