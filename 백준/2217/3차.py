# 배열에 저장해두고
# 작은 것부터 n, n-1, n-2 ... 곱해서 가장 큰 값 출력

import sys
input = sys.stdin.readline

N = int(input())

cnt = [i for i in range(N,0,-1)]
rope = []
result = []

for i in range(N):
    rope.append(int(input()))

for i in range(N):
    result.append(cnt[i]*rope[i])

print(max(result))