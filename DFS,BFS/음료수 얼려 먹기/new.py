# dfs는 모든 경우의 수를 찾을 경우에 사용되는 느낌

n, m = map(int, input().split())
arr = []
result = 0

for i in range(n):
    # line = list(map(int, input()))
    # arr.append(line)
    arr.append(list(map(int, input())))


def dfs(x, y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x >= n or x < 0 or y >= m or y < 0:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if arr[x][y] == 0:
        # 해당 노드 방문 처리
        arr[x][y] = 1
        # 상하좌우 모두 재귀적 호출
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)

        return True
    return False


# 모든 노드에 대해 음료수 채우기
for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행
        if dfs(i, j) == True:
            result += 1

print(result)
