n = int(input())
# plans = input().split()
plans = list(map(str, input().split()))

# 공간의 크기 지정
x = n
y = n

# 위치를 나타냄
px = 1
py = 1

for plan in plans:
    if plan == 'R':
        if py >= n:  # 우측으로 한 칸 진행할 경우
            py = n
            continue
        py += 1
    if plan == 'L':
        if py <= 1:
            py = 1
            continue
        py -= 1
    if plan == 'U':
        if px <= 1:
            px = 1
            continue
        px -= 1
    if plan == 'D':
        if px >= n:
            px = n
            continue
        px += 1

print(px, py)
