def solution(str1, str2):
    g1, g2 = [], []
    str1 = str1.upper()
    str2 = str2.upper()

    for i in range(len(str1)-1):
        element = str1[i:i+2]
        if element.isalpha():
            g1.append(element)

    for i in range(len(str2)-1):
        element = str2[i:i+2]
        if element.isalpha():
            g2.append(element)

    if len(g1) == 0 and len(g2) == 0:
        return 65536

    # 교집합
    g2_temp = g2.copy()
    intersection = intersections(g1, g2_temp)

    # 합집합
    g2_temp = g2.copy()
    union = unions(g1, g2_temp)

    answer = int(len(intersection) / len(union) * 65536)
    # 합집합 크기 = len(g1) + len(g2) - len(intersection) 로 한다면 훨씬 간단

    return answer

def intersections(set1, set2):
    result = []

    for i in set1:
        if i in set2:
            set2.remove(i)
            result.append(i)

    return result

def unions(set1, set2):
    result = []

    for i in set1:
        if i in set2:
            set2.remove(i)
        result.append(i)

    result += set2

    return result

# str1="FRANCE"
# str2="french"
# str1="handshake"
# str2="shake hands"
# str1="aa1+aa2"
# str2="AAAA12"
str1="E=M*C^2"
str2="e=m*c^2"
print(solution(str1, str2))