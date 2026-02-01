import sys
input = sys.stdin.readline

N, K = map(int, input().split())
wires = []

for _ in range(N):
    wire = int(input())
    wires.append(wire)

def can_process(L):
    total = 0
    for wire in wires:
        total += wire // L

    return total >= K

wires.sort()

start = 1
end = wires[-1]

while start <= end:
    mid = (start + end) // 2

    if can_process(mid):
        start = mid + 1
    else:
        end = mid - 1

print(end)