import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
result = []

# cards = deque()
# for i in range(n,0,-1):
#     cards.append(i)

cards = deque([i for i in range(1,n+1)])

while len(cards) != 0:
    result.append(cards.popleft())
    if len(cards) == 0:
        break
    card = cards.popleft()
    cards.append(card)
print(*result)