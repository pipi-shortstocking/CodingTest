grade = [[0] for _ in range(20)]

standard = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0,
            'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0, 'P': 0.0}
grade_sum = 0
score_sum = 0
aveg = 0

for i in range(20):
    grade[i] = list(map(str, input().split()))

    point = float(grade[i][1])
    user_grade = standard[grade[i][2]]

    if grade[i][2] != 'P' and 'F':
        score_sum += point
    grade_sum += point*user_grade

aveg = grade_sum/score_sum

# print(score_sum)
# print(grade_sum)

print(round(aveg, 6))
