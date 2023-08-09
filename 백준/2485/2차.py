import sys

input = sys.stdin.readline


def gcd(x, y):
    a = max(x, y)
    b = min(x, y)
    while b:
        a, b = b, a % b
    return a


n = int(input())
gap = []  # 가로수 사이의 간격을 저장한 배열
result = 0

t1 = int(input())
for i in range(n - 1):
    t2 = int(input())
    gap.append(t2 - t1)
    t1 = t2

g = gcd(gap[0], gap[1])
for i in range(1, len(gap)):
    g = gcd(g, gap[i])

for j in gap:
    result += int(j // g) - 1
print(result)
