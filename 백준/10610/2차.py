import sys
input = sys.stdin.readline

N = str(input().rstrip())
sum = 0
ans = ''

for i in N:
    sum += int(i)

if sum % 3 == 0:
    N = sorted(N, reverse=True)
    if len(N) == 1 or N[len(N)-1] != '0':
        print(-1)
    else:
        for i in N:
            ans += i
        print(int(ans))