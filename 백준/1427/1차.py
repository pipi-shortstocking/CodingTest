import sys
input = sys.stdin.readline

n = str(input().rstrip())
arr = []

for i in range(len(n)):
    arr.append(int(n[i]))

arr.sort(reverse=True)

for j in range(len(arr)):
    print(arr[j], end='')
