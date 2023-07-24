import sys, math
input = sys.stdin.readline

n = int(input())

fac = math.factorial(n)
str_fac = str(fac)
cnt = 0

for i in range(len(str_fac)-1,-1,-1):
    if str_fac[i] == '0':
        cnt += 1
    else:
        break

print(cnt)