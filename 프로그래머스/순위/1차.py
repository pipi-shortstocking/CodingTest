def solution(n, results):
    win_graph = [[] for _ in range(n+1)]
    lose_graph = [[] for _ in range(n+1)]
    answer = 0

    for a, b in results:
        win_graph[a].append(b)
        lose_graph[b].append(a)

    for i in range(1, n+1):
        win_visited = dfs(win_graph, i, set())
        lose_visited = dfs(lose_graph, i, set())

        if len(win_visited) + len(lose_visited) == n - 1:
            answer += 1

    return answer

def dfs(graph, node, visited):
    for next_node in graph[node]:
        if next_node not in visited:
            visited.add(next_node)
            dfs(graph, next_node, visited)

    return visited

n = 5
results = [[4,3],[4,2],[3,2],[1,2],[2,5]]
print(solution(n, results))