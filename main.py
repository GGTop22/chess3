def symbolsToIntCoord(k: str) -> (int, int):
    a = ord(k[0]) - ord('A') + 1
    b = int(k[1])
    return (a, b)


def isKnightJump(p1: (int, int), p2: (int, int)) -> bool:
    return (abs(p1[0] - p2[0]) == 2 and abs(p1[1] - p2[1]) == 1) or (
            abs(p1[0] - p2[0]) == 1 and abs(p1[1] - p2[1]) == 2)


def isBishopJump(p1: (int, int), p2: (int, int)) -> bool:
    return (abs(p1[0] - p2[0])) == (abs(p1[1] - p2[1]))


# def isQueenJump(p1: (int, int), p2: (int, int)) -> bool:
# return isBishopJump(p1, p2) or isRookJump(p1, p2)


# def isRookJump(p1: (int, int), p2: (int, int)) -> bool:
#  return (p1[0] == p2[0]) or (p1[1] == p2[1])


with open('INPUT.TXT', 'r') as input:
    s1, s2, s3, s4 = input.readline().strip().split()
# print(s1, s2, s3)
point1 = symbolsToIntCoord(s1)
point2 = symbolsToIntCoord(s2)
point3 = symbolsToIntCoord(s3)
point4 = symbolsToIntCoord(s4)
# print(point1, point2, point3, point4)

counter = 0
for i1 in range(1, 9):
    for i2 in range(1, 9):
        p = (i1, i2)
        if (isBishopJump(point1, p) or isBishopJump(point2, p) or isKnightJump(point3, p) or isKnightJump(point4,
                                                                                                          p)) and p != point1 and p != point2 and p != point3 and p != point4:
            counter += 1
            # print(p)
with open('OUTPUT.TXT', 'w') as output:
    output.write(str(counter))
