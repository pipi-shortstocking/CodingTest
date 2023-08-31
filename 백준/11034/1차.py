import sys
input = sys.stdin.readline

while True:
    try:
        a,b,c = map(int,input().split())

        term1 = b - a
        term2 = c - b

        print(max(term1, term2)-1)
    except:
        break