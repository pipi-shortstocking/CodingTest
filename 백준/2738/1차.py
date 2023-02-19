n, m = map(int, input().split())
arr1 = []
arr2 = []

for i in range(n):
    a = list(map(int, input().split()))
    arr1.append(a)

for i in range(n):
    a = list(map(int, input().split()))
    arr2.append(a)

for i in range(n):
    for j in range(m):
        print(arr1[i][j] + arr2[i][j], end=' ')
    print()
