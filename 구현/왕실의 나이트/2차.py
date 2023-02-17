loc = input()

col = int(ord(loc[0])-ord('a')+1)
row = int(loc[1])

count = 0

steps = [(-1, -2), (1, -2), (-1, 2), (1, 2),
         (-2, -1), (-2, 1), (2, -1), (2, 1)]

for step in steps:
    c_col = col+step[0]
    c_row = row+step[1]

    if c_col >= 1 and c_col <= 8 and c_row >= 1 and c_row <= 8:
        count += 1

print(count)
