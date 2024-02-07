import sys
input = sys.stdin.readline

# 약수 구하는 함수
def divisor(n) :
    result = []

    for i in range(1, int(n**(1/2)) + 1):
        if n % i == 0:
            result.append(i)
            if i < (n//i):
                result.append(n//i)
    result.sort()
    
    return result

t = int(input())

for _ in range(t):
    n = int(input())
    arr = [] # n보다 같거나 작은 모든 자연수의 각각의 약수를 담을 배열

    for i in range(n+1):
        arr += divisor(i) 
    print(sum(arr))