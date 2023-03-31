t = int(input())
coins = [25, 10, 5, 1]
# quarter dime nickel penny

for i in range(t):
    c = int(input())

    for coin in coins:
        print(c//coin, end=' ')
        c = c % coin
    print()
