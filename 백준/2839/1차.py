import sys
input = sys.stdin.readline

n = int(input())
count = 0

while n > 0:
    div = n // 3
    # print(n)
    count += 1
    # if (div%3) <= 0:
    #     break

print(count)