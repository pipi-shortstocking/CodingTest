import sys

input = sys.stdin.readline

n = str(input().rstrip())

arr = [0] * 10

for num in n:
    arr[int(num)] += 1

max = arr[0]
max_idx = 0
for i in range(10):
    if max < arr[i]:
        max = arr[i]
        max_idx = i

if max_idx == 6 or max_idx == 9:
    if (arr[6] + arr[9]) % 2 == 0:
        ans = (arr[6] + arr[9]) // 2
        print(ans)
    else:
        ans = (arr[6] + arr[9]) // 2 + 1
        print(ans)
else:
    print(max)
