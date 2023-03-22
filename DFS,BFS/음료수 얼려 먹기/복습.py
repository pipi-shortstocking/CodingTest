n, m = map(int, input().split())
arr = []
result = 0

for i in range(n):
    arr.append(list(map(int, input())))


def dfs(x, y):
    # 얼음 틀의 범위를 벗어났을 경우
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    
    # 처음 방문
    if arr[x][y] == 0:
        # 방문했음을 표시
        arr[x][y] = 1

        # 상하좌우 탐색
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)

        return True
    # 예외 상황 발생 시
    return False

# 모든 얼음틀 탐색
for i in range(n):
    for j in range(m):
        # True가 return 되면 무조건 1 추가
        if dfs(i, j) == True:
            result += 1

print(result)
