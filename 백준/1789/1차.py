import sys

input = sys.stdin.readline

s = int(input())
sum = 0
# arr = [0 for i in range(s + 1)]
cnt = 0

# i = 1
# while sum <= s:
#     sum += i
#     if sum > s:
#         break
#     i += 1
#     print(sum)

for i in range(1, s + 1):
    sum += i
    # arr[i] = 1
    cnt += 1
    if sum > s:
        sum -= i
        # arr[i] = 0
        cnt -= 1
    if sum == s:
        break

print(cnt)
