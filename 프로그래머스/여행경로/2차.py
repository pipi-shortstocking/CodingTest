def solution(tickets):
    visited = [False] * len(tickets)
    route = ["ICN"]

    tickets = sorted(tickets)

    def dfs(airport):
        if len(route) == len(tickets) + 1:
            return 

        for i in range(len(tickets)):
            if not visited[i] and tickets[i][0] == airport:
                visited[i] = True
                route.append(tickets[i][1])

                dfs(tickets[i][1])

                if len(route) != len(tickets) + 1:
                    visited[i] = False
                    route.pop()

    dfs("ICN")

    return route

# tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]

print(solution(tickets))