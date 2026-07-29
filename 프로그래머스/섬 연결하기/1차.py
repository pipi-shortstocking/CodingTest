def solution(n, costs):
    parent = [i for i in range(n)]
    costs = sorted(costs, key = lambda x: x[2])
    total = 0

    for a, b, cost in costs:
        if find(parent, a) != find(parent, b): # 사이클이 안 생기면
            union(parent, a, b) # 연결
            total += cost

    return total

# 합집합 찾기(find, union 함수)
def find(parent, x): # 부모 노드 찾기
    if parent[x] == x:
        return x

    return find(parent, parent[x])

def union(parent, a, b): # 합집합(트리구조)을 만들기
    root_a = find(parent, a)
    root_b = find(parent, b)

    parent[root_a] = root_b

n = 4
costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
print(solution(n, costs))