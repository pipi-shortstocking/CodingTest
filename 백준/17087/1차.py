import sys, math

input = sys.stdin.readline

n, s = map(int, input().split())  # 동생 수, 수빈이 위치

a = list(map(int, input().split()))  # 동생 위치

d = []  # 거리

for spot in a:
    dis = spot - s
    if dis < 0:
        d.append(-dis)
    elif dis > 0:
        d.append(dis)

d = set(d)
d = list(d)

if len(d) >= 2:
    gcd = math.gcd(d[0], d[1])

    for i in range(len(d) - 1):
        new_gcd = math.gcd(d[i], d[i + 1])
        if gcd < new_gcd:
            gcd = new_gcd
else:
    gcd = d[0]

print(gcd)
