import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

ans = []

for i in range(len(arr)):
    stack = arr[i + 1 :]
    result = []
    for num in stack[::-1]:
        if num > arr[i]:
            result.append(stack.pop())
        else:
            stack.pop()
    if result:
        ans.append(result.pop())
    else:
        ans.append(-1)

for j in ans:
    print(j, end=" ")
