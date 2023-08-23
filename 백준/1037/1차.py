import sys
input = sys.stdin.readline

num = int(input())
real = list(map(int,input().split()))

real.sort()
# print(real[0], real[-1])
print(real[0]*real[-1])