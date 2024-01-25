import sys

input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
F = []
NGF = [-1] * n
stack = []

for i in A:
    F.append(A.count(i))

stack.append(0)
for i in range(1, n):
    while stack and F[stack[-1]] < F[i]:
        NGF[stack.pop()] = A[i]
    stack.append(i)

print(*NGF)
