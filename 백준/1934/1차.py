import sys
input = sys.stdin.readline

#arr = []
result = []

def cal(N):
    div = 2
    square = int(N**0.5)
    arr=[]

    while div <= square:
        if N%div != 0:
            div+=1
        else:
            #print(div)
            arr.append(div)
            N/=div
    if N > 1:
        #print(int(N))
        arr.append(int(N))

        result.append(arr)
    #print(result)


t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    cal(a)
    cal(b)
print(result)

# import sys
# input = sys.stdin.readline

# #arr = []
# result = []

# def cal(a,b):
#     div = 2
#     square1 = int(a**0.5)
#     sqaure2 = int(b**0.5)
#     arr=[]

#     while (div <= square1) and (div <= sqaure2):
#         if (a%div != 0)and(b%div != 0):
#             div+=1
#         else:
#             #print(div)
#             arr.append(div)
#             a/=div
#     if a > 1:
#         #print(int(N))
#         arr.append(int(a))
#     if b > 1:
#         arr.append(int(b))

#         result.append(arr)
#     #print(result)


# t = int(input())

# for _ in range(t):
#     a, b = map(int, input().split())
#     cal(a,b)
# print(result)