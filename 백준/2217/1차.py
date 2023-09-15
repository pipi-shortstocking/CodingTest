import sys
input = sys.stdin.readline

n = int(input())
rope = []

for _ in range(n):
    rope.append(int(input()))

print(min(rope) * n)