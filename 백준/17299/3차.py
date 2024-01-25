import sys

input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
F = [0] * 1000001  # 1000000이면 런타임 에러! 인덱스 값은 0부터 시작하기 때문
NGF = [-1] * n
stack = []

for i in A:
    F[i] += 1

for i in range(n):
    while stack and F[A[stack[-1]]] < F[A[i]]:
        NGF[stack.pop()] = A[i]
    stack.append(i)

print(*NGF)
