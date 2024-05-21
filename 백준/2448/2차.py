n = int(input())


def draw(len):
    if len == 3:
        return ["  *  ", " * * ", "*****"]

    stars = draw(len // 2)
    arr = []
    for s in stars:
        arr.append(" " * (len // 2) + s + " " * (len // 2))
    for s in stars:
        arr.append(s + " " + s)
    return arr


print("\n".join(draw(n)))
