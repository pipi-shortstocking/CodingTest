import sys
input = sys.stdin.readline

n = int(input())
num_card = list(map(int, input().split()))

m = int(input())
check_list = list(map(int, input().split()))

dic = {}

for i in num_card:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

for i in check_list:
    if i in dic:
        print(dic[i], end=' ')
    else:
        print(0, end = ' ')