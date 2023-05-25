# set과 dictionary의 in연산을 통한 포함 여부 확인 시간복잡도는 O(1)

import sys

input = sys.stdin.readline

n = int(input())
n_arr = set(map(int, input().split()))
m = int(input())
m_arr = list(map(int, input().split()))

for num in m_arr:
    if num in n_arr:
        print(1)
    else:
        print(0)
