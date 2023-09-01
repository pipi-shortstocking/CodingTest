import sys
input = sys.stdin.readline

coins = [500,100,50,10,5,1]

money = int(input())
money = 1000 - money

cnt = 0

for coin in coins:
    cnt += money // coin
    money = money % coin

print(cnt)