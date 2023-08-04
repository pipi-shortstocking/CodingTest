import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    string = str(input().rstrip())

    # left, right = 0, 0

    # for ps in string:
    #     if ps == '(':
    #         left += 1
    #     elif ps == ")":
    #         right += 1
    
    # if left != right:
    #     print("NO")
    # # else:
    # #     print("YES")

    arr = [1,0] * (len(string)//2 + 1)
    for i in range(len(string)):
        if string[i] == '(':
            # arr[i*2] = '('
            try:
                num = arr.index(1)
            except:
                print(-1)
            arr[num] = '('
        elif string[i] == ')':
            try:
                num = arr.index(0)
            except:
                print(-1)
            arr[num] = ')'
    print(arr)
