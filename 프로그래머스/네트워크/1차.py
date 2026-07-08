def solution(n, computers):
    answer = 0
    visited = [False] * n

    def dfs(node):
        visited[node] = True

        for i in range(node + 1, n):
            if computers[node][i] == 1 and computers[i][node] == 1:
                dfs(i)

        return

    for i in range(n):
        if not visited[i]:
            dfs(i)           
            answer += 1

    return answer




n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]

# n = 3
# computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]

print(solution(n, computers))