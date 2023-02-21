n, m = map(int, input().split())
arr = [0]*n

for a in range(m):
    i, j, k = map(int, input().split())
    for b in range(i-1, j):
        arr[b] = k

for c in range(len(arr)):
    print(arr[c], end=' ')
