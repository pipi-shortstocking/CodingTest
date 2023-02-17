loc = input()

col = ord(loc[0]) - 96
row = int(loc[1])

count = 0

# 상
if (row-2) >= 1:
    # 좌
    if (col-1) >= 1:
        count += 1
    # 우
    if (col+1) <= 8:
        count += 1
# 하
if (row+2) <= 8:
    # 좌
    if (col-1) >= 1:
        count += 1
    # 우
    if (col+1) <= 8:
        count += 1
# 좌
if (col-2) >= 1:
    # 상
    if (row-1) >= 1:
        count += 1
    # 하
    if (row+1) <= 8:
        count += 1
# 우
if (col+2) <= 8:
    # 상
    if (row-1) >= 1:
        count += 1
    # 하
    if (row+1) <= 8:
        count += 1

print(count)
