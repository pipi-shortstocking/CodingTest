import sys

input = sys.stdin.readline

arr = str(input().rstrip())

arr = arr.replace("XXXX", "AAAA")
arr = arr.replace("XX", "BB")

if "X" in arr:
    print(-1)
else:
    print(arr)
