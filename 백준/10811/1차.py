n, m = map(int, input().split())
arr = [a+1 for a in range(n)]

for _ in range(m):
    i, j = map(int, input().split())
    temp = arr[i-1:j]
    temp.reverse()
    arr[i-1:j] = temp

for b in range(len(arr)):
    print(arr[b], end=' ')
