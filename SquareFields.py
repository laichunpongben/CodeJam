# Google Code Jam
# Practice Contests
# Practice Contest
# Problem B. Square Fields

inputTestCases = [0 for x in range(9)]

class TestCase:
    def __init__(self, n, k):
        self.pointCount = n
        self.squareCount = k
        self.points = [0 for x in range(n)]

class Point:
    def __init__(self, x, y):
        self.xCoordinate = x
        self.yCoordinate = y
        
class Square:
    def __init__(self, p1, p2):
        self.pointLeftTop = p1
        self.pointBottomRight = p2

def InitializeInputTestCases():
    global inputTestCases
    
    inputTestCases[0] = TestCase(7, 3)
    inputTestCases[0].points[0] = Point(57662, 11098)
    inputTestCases[0].points[1] = Point(7433, 12634)
    inputTestCases[0].points[2] = Point(48045, 56219)
    inputTestCases[0].points[3] = Point(1366, 25537)
    inputTestCases[0].points[4] = Point(6090, 15595)
    inputTestCases[0].points[5] = Point(13249, 38816)
    inputTestCases[0].points[6] = Point(21017, 10819)
    
    inputTestCases[1] = TestCase(7, 6)
    inputTestCases[1].points[0] = Point(45478, 25234)
    inputTestCases[1].points[1] = Point(15535, 30676)
    inputTestCases[1].points[2] = Point(24296, 47028)
    inputTestCases[1].points[3] = Point(18199, 28596)
    inputTestCases[1].points[4] = Point(35003, 54487)
    inputTestCases[1].points[5] = Point(30281, 16910)
    inputTestCases[1].points[6] = Point(45349, 37102)

    inputTestCases[2] = TestCase(7, 4)
    inputTestCases[2].points[0] = Point(1690, 845)
    inputTestCases[2].points[1] = Point(1690, 0)
    inputTestCases[2].points[2] = Point(0, 1690)
    inputTestCases[2].points[3] = Point(845, 1690)
    inputTestCases[2].points[4] = Point(1690, 2535)
    inputTestCases[2].points[5] = Point(1690, 3380)
    inputTestCases[2].points[6] = Point(2535, 1690)

    inputTestCases[3] = TestCase(3, 2)
    inputTestCases[3].points[0] = Point(3, 3)
    inputTestCases[3].points[1] = Point(3, 6)
    inputTestCases[3].points[2] = Point(6, 9)

    inputTestCases[4] = TestCase(7, 3)
    inputTestCases[4].points[0] = Point(2737, 1694)
    inputTestCases[4].points[1] = Point(1365, 1067)
    inputTestCases[4].points[2] = Point(1989, 2247)
    inputTestCases[4].points[3] = Point(2281, 2624)
    inputTestCases[4].points[4] = Point(1995, 3247)
    inputTestCases[4].points[5] = Point(3641, 1106)
    inputTestCases[4].points[6] = Point(2372, 2566)

    inputTestCases[5] = TestCase(7, 2)
    inputTestCases[5].points[0] = Point(76, 89)
    inputTestCases[5].points[1] = Point(44, 88)
    inputTestCases[5].points[2] = Point(82, 51)
    inputTestCases[5].points[3] = Point(45, 82)
    inputTestCases[5].points[4] = Point(57, 101)
    inputTestCases[5].points[5] = Point(69, 56)
    inputTestCases[5].points[6] = Point(98, 80)

    inputTestCases[6] = TestCase(7, 6)
    inputTestCases[6].points[0] = Point(2714, 34432)
    inputTestCases[6].points[1] = Point(54601, 32052)
    inputTestCases[6].points[2] = Point(40836, 1601)
    inputTestCases[6].points[3] = Point(38100, 36380)
    inputTestCases[6].points[4] = Point(34557, 23472)
    inputTestCases[6].points[5] = Point(22208, 58831)
    inputTestCases[6].points[6] = Point(2183, 1298)

    inputTestCases[7] = TestCase(5, 2)
    inputTestCases[7].points[0] = Point(1, 1)
    inputTestCases[7].points[1] = Point(2, 2)
    inputTestCases[7].points[2] = Point(3, 3)
    inputTestCases[7].points[3] = Point(6, 6)
    inputTestCases[7].points[4] = Point(7, 8)

    inputTestCases[8] = TestCase(4, 2)
    inputTestCases[8].points[0] = Point(864, 25548)
    inputTestCases[8].points[1] = Point(23328, 12075)
    inputTestCases[8].points[2] = Point(22093, 26174)
    inputTestCases[8].points[3] = Point(10708, 39349)

def CreateSquare(point, length, direction):
    p1 = 0
    p2 = 0
    if (direction == 0):
        p1 = Point(point.xCoordinate, point.yCoordinate + length)
        p2 = Point(point.xCoordinate + length, point.yCoordinate)
    if (direction == 1):
        p1 = point
        p2 = Point(point.xCoordinate + length, point.yCoordinate - length)
    if (direction == 2):
        p1 = Point(point.xCoordinate - length, point.yCoordinate)
        p2 = Point(point.xCoordinate, point.yCoordinate - length)
    if (direction == 3):
        p1 = Point(point.xCoordinate - length, point.yCoordinate + length)
        p2 = point
    return Square(p1, p2)

def IsPointInSquare(point, square):
    return (square.pointLeftTop.xCoordinate <= point.xCoordinate) and \
    (point.xCoordinate <= square.pointBottomRight.xCoordinate) and \
    (square.pointLeftTop.yCoordinate <= point.yCoordinate) and \
    (point.yCoordinate <= square.pointBottomRight.yCoordinate)
    
def Choose_iter(elements, length):
    for i in xrange(len(elements)):
        if length == 1:
            yield (elements[i],)
        else:
            for next in choose_iter(elements[i+1:len(elements)], length-1):
                yield (elements[i],) + next
                
def Choose(n, k):
    return list(choose_iter(n, k))
        
def CanSquareLengthCoverAllPoints(testCase, squareLength):
    for pointList in Choose_iter(testCase.points, testCase.squareCount):
        for point in pointList:
            CreateSquare(point, squareLength, 0)
    
    
    for x in range(testCase.squareCount):
        C
        checkIfPointCovered = 0
        
        for point in range(testCase.points):
            if (true): checkIfPointCovered += 1
    
def ComputeMinSquareLength(testCase):
    checkIfPointCovered = 0
    while (checkIfPointCovered < testCase.pointCount):
    return 0
    
def PrintAllResults():
    InitializeInputTestCases()
    
PrintAllResults()
