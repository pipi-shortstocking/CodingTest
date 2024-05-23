n = int(input())
arr = []
ans = 0

for _ in range(n):
    h = int(input())

    while len(arr) != 0 and arr[-1] <= h:
        arr.pop()
    ans += len(arr)
    arr.append(h)

print(ans)
