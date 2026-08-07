from collections import deque

def solution(numbers, hand):
    answer = ""
    l_loc = 10
    r_loc = 12

    for num in numbers:
        if num == 0:
            num = 11

        if num in (1, 4 ,7):
            answer += "L"
            l_loc = num
        elif num in (3, 6, 9):
            answer += "R"
            r_loc = num
        else:
            l_gap = bfs(l_loc, num)
            r_gap = bfs(r_loc, num)

            if l_gap != -1 or r_gap != -1:
                if l_gap < r_gap:
                    answer += "L"
                    l_loc = num
                elif l_gap > r_gap:
                    answer += "R"
                    r_loc = num
                else:
                    if hand == "right":
                        answer += "R"
                        r_loc = num
                    else:
                        answer += "L"
                        l_loc = num

    return answer

def bfs(loc, num):
    keypad = [[1,2,3], [4,5,6], [7,8,9], [10,11,12]]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()
    visited = [[-1] * 3 for _ in range(4)]
    goal_x, goal_y = 0, 0

    for i in range(4):
        for j in range(3):
            if keypad[i][j] == loc:
                queue.append((i, j))
                visited[i][j] = 0

            if keypad[i][j] == num:
                goal_x, goal_y = i, j

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx < 4 and ny >= 0 and ny < 3:
                if visited[nx][ny] == -1:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))

    return visited[goal_x][goal_y]

# numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
# hand = "right"
# numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
# hand = "left"
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
hand = "right"

print(solution(numbers, hand))