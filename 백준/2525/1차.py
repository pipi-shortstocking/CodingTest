h, m = map(int, input().split())
p = int(input())

h += (m+p)//60
m = (m+p) % 60

if h > 23:
    h -= 24

print(h, m)
