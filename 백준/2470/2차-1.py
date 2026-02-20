import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

arr.sort()

start, end = 0, n - 1
target = 0
diff = float('inf')

answer = (arr[start], arr[end])

while start < end:
    temp_sum = arr[start] + arr[end]
    temp_diff = abs(temp_sum)

    if temp_diff < diff:
        diff = temp_diff
        answer = (arr[start], arr[end])

    if temp_sum < target:
        start += 1
    elif temp_sum > target:
        end -= 1
    else:
        break

print(* answer)