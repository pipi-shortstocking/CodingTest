import sys
input = sys.stdin.readline

v = int(input())
people = str(input().rstrip())

cnt_A = people.count('A')
cnt_B = people.count('B')

if cnt_A > cnt_B:
    print('A')
elif cnt_A < cnt_B:
    print('B')
elif cnt_A == cnt_B:
    print('Tie')