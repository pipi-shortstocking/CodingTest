import sys

input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
F = []
NGF = [-1] * n
stack = []

stack.append(0)
F.append(A.count(A[0]))
for i in range(1, n):
    F.append(A.count(A[i]))
    while stack and F[stack[-1]] < F[i]:
        NGF[stack.pop()] = A[i]
    stack.append(i)

print(*NGF)
