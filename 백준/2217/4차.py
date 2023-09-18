import sys
input = sys.stdin.readline

N = int(input())

cnt = [i for i in range(N,0,-1)]
rope = []
result = []

for i in range(N):
    rope.append(int(input()))
rope.sort()

for i in range(N):
    result.append(cnt[i]*rope[i])

print(max(result))