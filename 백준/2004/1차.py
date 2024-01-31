import sys, math

input = sys.stdin.readline

n, m = map(int, input().split())

result = math.factorial(n) / math.factorial(m) * math.factorial(n - m)

str_result = str(result)
cnt = 0

for i in range(len(str_result) - 1, -1, -1):
    if str_result[i] == "0":
        cnt += 1

print(str_result)
print(cnt)
