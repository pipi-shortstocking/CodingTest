import sys
input = sys.stdin.readline

a,b = map(str,input().split())

new_a1 = a.replace('6', '5');
new_b1 = b.replace('6', '5');

min = int(new_a1) + int(new_b1);

new_a2 = a.replace('5', '6');
new_b2 = b.replace('5', '6');

max = int(new_a2) + int(new_b2);

print(min, max)