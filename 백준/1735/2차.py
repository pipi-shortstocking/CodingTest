# 기약분수 고려 추가

import sys

input = sys.stdin.readline

def gcd(a,b):
    while b != 0:
        tmp = a%b
        a = b
        b = tmp
    return a

n1, d1 = map(int, input().split())
n2, d2 = map(int, input().split())

# n1 = n1/gcd(n1,d1)
# d1 = d1/gcd(n1,d1)

# n2 = n2/gcd(n2,d2)
# d2 = d2/gcd(n2,d2)

d = int(d1*d2/gcd(d1,d2)) # 분모
mul1 = int(d / d1)
mul2 = int(d / d2)

n = n1 * mul1 + n2 * mul2

d = int(d/gcd(n,d))
n = int(n/gcd(n,d))

print(n, d)
