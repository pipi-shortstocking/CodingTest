import sys
input = sys.stdin.readline

num = int(input())
real = list(map(int,input().split()))

print(min(real)*max(real))