import sys
input = sys.stdin.readline

N = str(input().rstrip())
sum = 0
ans=''

if '0' not in N:
    print(-1)
else:
    for i in N:
        sum += int(i)

    if sum % 3 != 0:
        print(-1)
    else:
        N = sorted(N, reverse=True)
        for i in N:
            ans += i
        print(int(ans))