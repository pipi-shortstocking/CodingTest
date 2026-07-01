## 재귀형
def dfs_recursion(graph, node, visited):
    # 현재 노드 방문 처리
    visited[node] = True

    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[node]:
        if not visited[i]:
            dfs_recursion(graph, i, visited)

## 스택형
def dfs_stack(start, graph, N):
    visited = [False] * (N + 1) # 방문 여부 리스트
    stack = [start] # 시작 노드를 스택에 넣기

    while stack:
        v = stack.pop()

        if not visited[v]:
            visited[v] = True # 방문 처리

            for u in graph[v]:
                stack.append(u)