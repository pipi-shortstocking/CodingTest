import sys
input = sys.stdin.readline

n = int(input())
g = 0

# n이 10일 때, 
# 1 : 10 // 1 = 10개
# 2 : 10 // 2 = 5개
# 3 : 10 // 3 = 3개
# ...
# 10 : 10 // 10 = 1개

for i in range(1,n+1):
    g += i * (n//i) 
print(g)