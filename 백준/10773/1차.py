import sys
input = sys.stdin.readline

k = int(input())
arr = []

for _ in range(k):
    num = int(input())

    if num == 0:
        arr.pop()
    else:
        arr.append(num)
print(sum(arr))