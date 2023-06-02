import sys

input = sys.stdin.readline

n, k = map(int, input().split())
arr = [i + 1 for i in range(n)]
result = []
index = 0

for i in range(n):
    index += k - 1
    # print(index)
    if index >= len(arr):
        index = index % len(arr)
        # print(index)
    result.append(str(arr[index]))
    arr.pop(index)
    # print(result)
    # print(arr)

print("<", ", ".join(result), ">", sep="")
