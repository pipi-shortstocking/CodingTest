n, k = map(int, input().split())
arr = []

for i in range(1, n+1):
    if n % i == 0:
        # print(int(n/i))
        arr.append(i)

# print(arr)
if k <= len(arr):
    print(arr[k-1])
else:
    print(0)
