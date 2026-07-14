def solution(tickets):
    stack = ["ICN"] # 항상 ICN에서 출발
    visited = [False] * len(tickets)
    route = []

    while stack:
        airport = stack.pop()

        for i in range(len(tickets)):
            if not visited[i] and tickets[i][0] == airport:
                visited[i] = True
                stack.append(tickets[i][1])
                route.append(tickets[i][0])

    return route

tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
# tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]

print(solution(tickets))