from collections import deque
import sys

n = int(input())

cards = deque([i for i in range(1,n+1)])

while len(cards) != 0:
    result = cards.popleft()
    if len(cards) == 0:
        break
    card = cards.popleft()
    cards.append(card)
print(result)