n, k = map(int, input().split())
count = 0

while n != 1:
    if n % k == 0:
        n = n/k
        count += 1
    else:
        n -= 1  # N의 범위가 10만 이하 이므로 일일이 1씩 빼도 문제 해결 가능(N이 100억 이상의 큰 수일 경우 고려)
        count += 1

print(count)
