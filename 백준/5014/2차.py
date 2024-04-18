from collections import deque

f, s, g, u, d = map(int, input().split())

# 스타트링크의 위치와 강호의 위치가 같을 경우 처리 필요
if s == g:
    print(0)
    exit()

building = [-1 for _ in range(f)]
queue = deque()
dx = [u, -d]

queue.append(s - 1)  # 배열에서는 1층의 위치가 0
building[s - 1] = 0
while queue:
    x = queue.popleft()
    for i in range(2):
        nx = x + dx[i]

        if 0 <= nx < f and building[nx] == -1:
            building[nx] = building[x] + 1
            if nx == g - 1:
                print(building[nx])
                # print(building)
                exit()
            queue.append(nx)

print("use the stairs")
# print(building)
