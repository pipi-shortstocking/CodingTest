import sys, math

input = sys.stdin.readline

n, s = map(int, input().split())  # 동생 수, 수빈이 위치

a = list(map(int, input().split()))  # 동생 위치

d = []  # 거리

for spot in a:
    dis = spot - s
    if dis != 0:
        d.append(abs(dis))

# d = set(d)
# d = list(d) # 따로 처리를 안하는 것이 더 빠름
gcd = 0

for i in range(len(d)):
    gcd = math.gcd(gcd, d[i])

print(gcd)
