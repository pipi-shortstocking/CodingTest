import sys
input = sys.stdin.readline

n = int(input())
ans = []

for _ in range(n):
    ans.append(int(input()))

cnt_0 = ans.count(0)
cnt_1 = ans.count(1)

if cnt_0 > cnt_1:
    print("Junhee is not cute!")
else:
    print("Junhee is cute!")