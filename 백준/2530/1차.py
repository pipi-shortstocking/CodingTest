h, m, s = map(int, input().split())
p = int(input())

m += (s+p)//60
s = (s+p) % 60

h += m//60
m %= 60

# if h > 23:
#     h -= 24 # 이렇게 하면 틀림

h %= 24  # 이렇게 하면 통과

print(h, m, s)
