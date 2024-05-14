n = int(input())
arr = []
ans = [0, 0, 0]  # -1, 0, 1

for _ in range(n):
    arr.append(list(map(int, input().split())))


def check(x, y, n):
    for i in range(x, x + n):
        for j in range(y, y + n):
            if arr[x][y] != arr[i][j]:
                return False
    return True


def solve(x, y, z):
    if check(x, y, z):
        ans[arr[x][y] + 1] += 1
        return
    else:
        n = z // 3
        for i in range(3):
            for j in range(3):
                solve(x + i * n, y + j * n, n)


solve(0, 0, n)
for a in ans:
    print(a)
