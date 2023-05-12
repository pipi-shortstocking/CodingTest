import sys
input = sys.stdin.readline

n = int(input())
num_card = list(map(int, input().split()))

m = int(input())
check_list = list(map(int, input().split()))

for i in check_list:
    if i in num_card:
        print(1, end=' ')
    else:
        print(0, end=' ')