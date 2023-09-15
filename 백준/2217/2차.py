import sys
input = sys.stdin.readline

n = int(input())
rope = []

for _ in range(n):
    rope.append(int(input()))

seq_1 = min(rope) * n
seq_2 = max(rope)

if seq_1 < seq_2:
    print(seq_2)
else:
    print(seq_1)