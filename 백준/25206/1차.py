#grade = [[0]*3 for _ in range(3)]
grade = [[0] for _ in range(3)]

for i in range(3):
    # sub, sco, gra = map(str, input().split())
    # # grade[i].append(sub)
    # grade[i] = sub
    # grade[i].append(float(sco))
    # grade[i].append(gra)

    grade[i] = list(map(str, input().split()))

print(grade)
