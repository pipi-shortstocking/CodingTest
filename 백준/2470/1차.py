import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

arr.sort()

start, end = 0, n - 1
target = 0

diff = target - (arr[start] + arr[end])
solutions = [(start, end)]

while start < end:
    temp_sum = arr[start] + arr[end]
    temp_diff = abs(target - temp_sum)

    if temp_sum == target:
        solutions.append((start, end))
        break
    elif temp_sum < target:
        if temp_diff < diff:
            diff = temp_diff
            solutions.append((start, end))
        start += 1
    else:
        if temp_diff < diff:
            diff = temp_diff
            solutions.append((start, end))
        end -= 1

ans = solutions.pop()
print(arr[ans[0]], arr[ans[1]])