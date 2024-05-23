# 시간초과

n = int(input())
buildings = []

for _ in range(n):
    buildings.append(int(input()))

cnt = 0
for i in range(n):
    for j in range(i + 1, n):
        if buildings[i] > buildings[j]:
            cnt += 1
        else:
            break

print(cnt)
