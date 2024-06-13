from itertools import combinations

while True:
    arr = list(map(int, input().split()))

    if arr[0] == 0:
        break
    k = arr[0]
    s = arr[1 : k + 1]

    ans = list(combinations(s, 6))

    for a in ans:
        print(*a)
    print()
