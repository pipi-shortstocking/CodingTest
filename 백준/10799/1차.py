import sys
input = sys.stdin.readline

raser = str(input().rstrip())
pointer_loc = []

for i in range(len(raser)):
    # 포인터 위치 저장
    if raser[i] == '(' and raser[i+1] == ')':
        pointer_loc.append([i,i+1])
    
    elif raser[i] == '(':
        