import sys, math
input = sys.stdin.readline

n,k = map(int, input().split())

# 분자 numerator
num = math.factorial(n)

# 분모 denominator
den = math.factorial(k) * math.factorial(n-k)

print(int(num/den))