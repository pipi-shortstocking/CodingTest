import sys, math

input = sys.stdin.readline

n1, d1 = map(int, input().split())
n2, d2 = map(int, input().split())

div = math.gcd(d1, d2)  # 분모들의 최대공약수
d = int(d1 * d2 / div)  # 분모
mul1 = int(d / d1)
mul2 = int(d / d2)

n = n1 * mul1 + n2 * mul2

print(n, d)
