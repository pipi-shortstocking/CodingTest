import sys, math
input = sys.stdin.readline

n = int(input())
loc_arr = [] # 각 가로수 간의 간격 저장

loc = int(input())
for _ in range(n-1):
    next_loc = int(input())
    loc_arr.append(next_loc-loc)
    loc = next_loc

GCD = math.gcd(loc_arr[0],loc_arr[1])
for i in range(2, len(loc_arr)-2):
    #print(loc_arr[i], loc_arr[i+1])
    #GCD = math.gcd(loc_arr[i],loc_arr[i+1])
    GCD = math.gcd(GCD, loc_arr[i])

# print(GCD)

count=[]
for i in loc_arr:
    count.append(int(i/GCD)-1)

print(sum(count))