import sys

input = sys.stdin.readline

n = int(input())
n_arr = list(map(int, input().split()))
m = int(input())
m_arr = list(map(int, input().split()))

for num in m_arr:
    if num in n_arr:
        print(1)
    else:
        print(0)
