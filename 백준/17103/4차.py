import sys, math
from itertools import combinations_with_replacement

input = sys.stdin.readline
# sum_arr=[]
cnt = 0


def pri(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


t = int(input())

for _ in range(t):
    num = int(input())
    pri_arr = [i for i in range(2, num) if pri(i)]
    # print(pri_arr)
    # for p in combinations_with_replacement(pri_arr, 2):
    #    print(p, sum(p), end=" ")
    for p in combinations_with_replacement(pri_arr, 2):
        # print(p)
        if sum(p) == num:
            # sum_arr.append(p)
            cnt += 1

    print(cnt)
    pri_arr = []
    cnt = 0
