n,m = map(int, input().split())
arr=[a+1 for a in range(n)]

for _ in range(m):
    i,j = map(int, input().split())
    arr[i-1],arr[j-1] = arr[j-1],arr[i-1]

for b in range(len(arr)):
    print(arr[b], end=' ')