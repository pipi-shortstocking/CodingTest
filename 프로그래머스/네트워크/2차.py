def solution(n, computers):
    answer = 0
    visited = [False] * n

    def dfs(node):
        visited[node] = True

        for i in range(n):
            # node + 1부터 시작하면 node보다 인덱스가 작은 노드는 탐색 X
            # ex) node = 2일 때 0번, 1번 컴퓨터와 연결되어 있어도 확인 X
            if not visited[i] and computers[node][i] == 1 and computers[i][node] == 1:
                dfs(i)

    for i in range(n):
        if not visited[i]:
            dfs(i)           
            answer += 1

    return answer

# n = 3
# computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]

n = 3
computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]

print(solution(n, computers))