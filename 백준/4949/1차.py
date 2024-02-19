import sys
input = sys.stdin.readline

while True:
    string = str(input().rstrip('\n'))
    stk = []

    if len(string) == 1 and string == ".":
        break
    
    for ch in string:
        if ch == "(" or ch == "[":
            stk.append(ch)
        elif ch == ")":
            if len(stk) != 0 and stk[-1] == "(":
                stk.pop()
        elif ch == "]":
            if len(stk) != 0 and stk[-1] ==  "[":
                stk.pop()
        
    if len(stk) == 0:
        print("yes")
    else:
        print("no")