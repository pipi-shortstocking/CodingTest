n, m = map(int, input().split())
arr = list(map(int, input().split()))

count = 0

while True:
    i, j = map(int, input().split())
    print(sum(arr[i-1:j]))
    count += 1

    if count == m:
        break
