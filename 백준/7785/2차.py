import sys

input = sys.stdin.readline

n = int(input())
arr_name = []
arr = {}

for _ in range(n):
    name, state = map(str, input().rstrip().split())
    arr_name.append(name)
    arr[name] = state

arr_name = list(set(arr_name))

for i in arr_name:
    if arr[i] == "leave":
        del arr[i]

# print(arr.keys(), end=" ")
# print(len(arr))

for i in sorted(arr.keys(), reverse=True):
    print(i)
