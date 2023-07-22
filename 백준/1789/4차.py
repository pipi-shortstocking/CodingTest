import sys

input = sys.stdin.readline

s = int(input())
sum = 0
cnt = 0

for i in range(1, s + 1):
    sum += i
    cnt += 1
    if sum > s:
        cnt -= 1
        # print(sum)
        break

print(cnt)
