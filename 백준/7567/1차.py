import sys
input = sys.stdin.readline

dishes = input().rstrip()
prev = '*'
height = 0

for dish in dishes:
    if dish != prev:
        height += 10
    else:
        height += 5
    
    prev = dish

print(height)