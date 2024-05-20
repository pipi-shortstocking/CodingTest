n = int(input())
arr = []
ans = ""

for _ in range(n):
    arr.append(list(map(int, input())))


def check(x, y, n):
    for i in range(x, x + n):
        for j in range(y, y + n):
            if arr[x][y] != arr[i][j]:
                return False
    return True


def solve(x, y, z):
    global ans
    temp = ""
    if check(x, y, z):
        ans += str(arr[x][y])
    else:
        n = z // 2
        for i in range(2):
            for j in range(2):
                solve(x + i * n, y + j * n, n)

    ans += temp


solve(0, 0, n)
print(ans)
