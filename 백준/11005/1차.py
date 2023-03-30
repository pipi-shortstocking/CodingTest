n, b = map(int, input().split())
rev_mod = ''

while n > 0:
    n, mod = divmod(n, b)
    if mod >= 10:
        mod = chr(mod+55)
    rev_mod += str(mod)

print(rev_mod[::-1])
