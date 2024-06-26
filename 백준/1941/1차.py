from collections import deque

stu = []
for _ in range(5):
    stu.append(list(input()))


def bfs():
    queue = deque()
