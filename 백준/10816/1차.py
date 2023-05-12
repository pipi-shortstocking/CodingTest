import sys
input = sys.stdin.readline

n = int(input())
num_card = list(map(int, input().split()))

m = int(input())
check_list = list(map(int, input().split()))

dic = {}

for i in check_list:
    dic[i] = 0

for i in num_card:
    dic[i] = num_card.count(i)

for i in check_list:
    print(dic[i], end=' ')