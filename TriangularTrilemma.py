# Google Code Jam
# Practice Contests
# Code Jam Beta 2008
# Problem A. Triangular Trilemma

from math import pi
from math import acos

inputTestCases = [0 for x in range(100)]

class Point:
    def __init__(self, x, y):
        self.xCoordinate = x
        self.yCoordinate = y
        
    def __eq__(self, other):
        return self.xCoordinate == other.xCoordinate and \
            self.yCoordinate == other.yCoordinate
        
class Triangle:
    def __init__(self, x1, y1, x2, y2, x3, y3):
        p1 = Point(x1, y1)
        p2 = Point(x2, y2)
        p3 = Point(x3, y3)
        self.point1 = p1
        self.point2 = p2
        self.point3 = p3
        
        isSeperatedPoints = IsSeperatedPoints(self.point1, self.point2, self.point3)
        isZeroArea = IsZeroArea(self.point1, self.point2, self.point3)
        if (isSeperatedPoints and not isZeroArea): 
            self.length1 = ComputeLength(self.point1, self.point2)
            self.length2 = ComputeLength(self.point1, self.point3)
            self.length3 = ComputeLength(self.point2, self.point3)
            
            self.angle1 = ComputeAngle(self.length1, self.length2, self.length3)
            self.angle2 = ComputeAngle(self.length1, self.length3, self.length2)
            self.angle3 = ComputeAngle(self.length2, self.length3, self.length1)
            
    def ComputeResult(self):
        if (not IsSeperatedPoints(self.point1, self.point2, self.point3)): return "not a triangle"
        elif (IsZeroArea(self.point1, self.point2, self.point3)): return "not a triangle"
        elif (HasZeroAngle(self.angle1, self.angle2, self.angle3)): return "not a triangle"
        elif (HasOverPiAngle(self.angle1, self.angle2, self.angle3)): return "not a triangle"
        else: 
            lengthType = ComputeLengthType(self.length1, self.length2, self.length3)
            angleType = ComputeAngleType(self.angle1, self.angle2, self.angle3)
            return lengthType + " " + angleType + " triangle"
        
def InitializeInputTestCases():
    global inputTestCases
    
    inputTestCases[0] = Triangle(0, 0, 0, 4, 1, 2)
    inputTestCases[1] = Triangle(1, 1, 1, 4, 3, 2)
    inputTestCases[2] = Triangle(2, 2, 2, 4, 4, 3)
    inputTestCases[3] = Triangle(3, 3, 3, 4, 5, 3)
    inputTestCases[4] = Triangle(4, 4, 4, 5, 5, 6)
    inputTestCases[5] = Triangle(5, 5, 5, 6, 6, 5)
    inputTestCases[6] = Triangle(6, 6, 6, 7, 6, 8)
    inputTestCases[7] = Triangle(7, 7, 7, 7, 7, 7)
    inputTestCases[8] = Triangle(0, 1, 0, 1, 2, 4)
    inputTestCases[9] = Triangle(0, 1, 2, 4, 0, 1)
    inputTestCases[10] = Triangle(2, 4, 0, 1, 0, 1)
    inputTestCases[11] = Triangle(0, 0, 1, 1, 2, 0)
    inputTestCases[12] = Triangle(0, 0, 2, 2, 3, 1)
    inputTestCases[13] = Triangle(0, 0, 1, 2, 3, 1)
    inputTestCases[14] = Triangle(0, 0, 1, 2, 5, 0)
    inputTestCases[15] = Triangle(1, 0, 2, 3, 4, 9)
    inputTestCases[16] = Triangle(0, 0, 4, 1, 6, 7)
    inputTestCases[17] = Triangle(2, 0, 5, 7, 4, 8)
    inputTestCases[18] = Triangle(7, 4, 1, 8, 3, 1)
    inputTestCases[19] = Triangle(5, 6, 8, 7, 3, 7)
    inputTestCases[20] = Triangle(8, 1, 4, 6, 5, 2)
    inputTestCases[21] = Triangle(4, 3, 7, 3, 0, 5)
    inputTestCases[22] = Triangle(2, 5, 8, 7, 6, 7)
    inputTestCases[23] = Triangle(7, 6, 0, 1, 2, 9)
    inputTestCases[24] = Triangle(9, 3, 5, 6, 2, 6)
    inputTestCases[25] = Triangle(8, 2, 2, 0, 0, 9)
    inputTestCases[26] = Triangle(8, 0, 3, 5, 2, 7)
    inputTestCases[27] = Triangle(5, 0, 5, 1, 2, 0)
    inputTestCases[28] = Triangle(1, 5, 2, 7, 1, 9)
    inputTestCases[29] = Triangle(9, 0, 4, 3, 2, 1)
    inputTestCases[30] = Triangle(2, 9, 9, 8, 1, 1)
    inputTestCases[31] = Triangle(7, 6, 7, 0, 0, 2)
    inputTestCases[32] = Triangle(3, 8, 5, 4, 1, 3)
    inputTestCases[33] = Triangle(3, 2, 7, 4, 7, 1)
    inputTestCases[34] = Triangle(1, 3, 4, 1, 5, 5)
    inputTestCases[35] = Triangle(3, 1, 9, 7, 0, 1)
    inputTestCases[36] = Triangle(3, 3, 7, 2, 4, 5)
    inputTestCases[37] = Triangle(5, 3, 8, 1, 4, 2)
    inputTestCases[38] = Triangle(3, 7, 9, 8, 4, 0)
    inputTestCases[39] = Triangle(2, 7, 0, 7, 8, 6)
    inputTestCases[40] = Triangle(2, 1, 0, 8, 1, 2)
    inputTestCases[41] = Triangle(1, 6, 5, 9, 3, 6)
    inputTestCases[42] = Triangle(3, 0, 6, 8, 3, 0)
    inputTestCases[43] = Triangle(1, 4, 8, 6, 1, 2)
    inputTestCases[44] = Triangle(2, 4, 4, 8, 0, 1)
    inputTestCases[45] = Triangle(8, 9, 5, 4, 1, 5)
    inputTestCases[46] = Triangle(4, 9, 9, 6, 2, 4)
    inputTestCases[47] = Triangle(9, 3, 5, 7, 3, 5)
    inputTestCases[48] = Triangle(2, 3, 3, 9, 7, 6)
    inputTestCases[49] = Triangle(2, 1, 2, 2, 0, 8)
    inputTestCases[50] = Triangle(2, 0, 2, 2, 9, 7)
    inputTestCases[51] = Triangle(2, 7, 3, 3, 1, 6)
    inputTestCases[52] = Triangle(1, 2, 4, 1, 6, 2)
    inputTestCases[53] = Triangle(8, 0, 6, 3, 4, 5)
    inputTestCases[54] = Triangle(8, 7, 2, 5, 2, 2)
    inputTestCases[55] = Triangle(7, 2, 4, 7, 7, 3)
    inputTestCases[56] = Triangle(6, 9, 1, 5, 0, 5)
    inputTestCases[57] = Triangle(8, 9, 1, 4, 9, 4)
    inputTestCases[58] = Triangle(0, 6, 9, 1, 4, 0)
    inputTestCases[59] = Triangle(7, 9, 3, 3, 0, 4)
    inputTestCases[60] = Triangle(6, 1, 0, 0, 6, 3)
    inputTestCases[61] = Triangle(6, 8, 4, 6, 3, 4)
    inputTestCases[62] = Triangle(3, 9, 5, 7, 9, 2)
    inputTestCases[63] = Triangle(1, 0, 5, 9, 7, 0)
    inputTestCases[64] = Triangle(8, 8, 7, 8, 1, 4)
    inputTestCases[65] = Triangle(4, 9, 2, 9, 1, 3)
    inputTestCases[66] = Triangle(2, 0, 0, 0, 9, 0)
    inputTestCases[67] = Triangle(0, 4, 3, 5, 4, 4)
    inputTestCases[68] = Triangle(6, 8, 6, 7, 4, 4)
    inputTestCases[69] = Triangle(4, 4, 4, 5, 1, 8)
    inputTestCases[70] = Triangle(6, 1, 9, 1, 6, 4)
    inputTestCases[71] = Triangle(0, 4, 3, 0, 5, 2)
    inputTestCases[72] = Triangle(5, 9, 8, 5, 9, 2)
    inputTestCases[73] = Triangle(4, 6, 6, 8, 9, 6)
    inputTestCases[74] = Triangle(9, 5, 9, 1, 7, 6)
    inputTestCases[75] = Triangle(0, 7, 3, 8, 3, 5)
    inputTestCases[76] = Triangle(6, 4, 4, 4, 4, 3)
    inputTestCases[77] = Triangle(2, 8, 8, 7, 5, 8)
    inputTestCases[78] = Triangle(4, 0, 5, 1, 5, 1)
    inputTestCases[79] = Triangle(9, 2, 1, 2, 2, 5)
    inputTestCases[80] = Triangle(0, 3, 2, 2, 4, 5)
    inputTestCases[81] = Triangle(1, 4, 8, 9, 8, 0)
    inputTestCases[82] = Triangle(0, 8, 9, 6, 5, 3)
    inputTestCases[83] = Triangle(3, 3, 7, 0, 6, 4)
    inputTestCases[84] = Triangle(3, 5, 6, 2, 9, 8)
    inputTestCases[85] = Triangle(9, 0, 1, 9, 4, 8)
    inputTestCases[86] = Triangle(9, 9, 1, 5, 7, 7)
    inputTestCases[87] = Triangle(4, 9, 0, 7, 1, 1)
    inputTestCases[88] = Triangle(3, 6, 7, 2, 2, 0)
    inputTestCases[89] = Triangle(7, 7, 6, 0, 1, 7)
    inputTestCases[90] = Triangle(5, 7, 5, 3, 1, 2)
    inputTestCases[91] = Triangle(3, 8, 1, 3, 0, 0)
    inputTestCases[92] = Triangle(6, 3, 1, 1, 3, 5)
    inputTestCases[93] = Triangle(9, 0, 9, 7, 3, 6)
    inputTestCases[94] = Triangle(9, 9, 4, 2, 7, 4)
    inputTestCases[95] = Triangle(0, 4, 7, 0, 7, 8)
    inputTestCases[96] = Triangle(9, 6, 9, 5, 6, 9)
    inputTestCases[97] = Triangle(4, 7, 8, 1, 3, 3)
    inputTestCases[98] = Triangle(0, 3, 0, 4, 7, 0)
    inputTestCases[99] = Triangle(5, 8, 8, 3, 8, 5)

def IsSeperatedPoints(p1, p2, p3):
    if ((p1 == p2) or (p1 == p3) or (p2 == p3)): return False
    else: return True
    
def ComputeArea(p1, p2, p3):
    return (p1.xCoordinate * (p2.yCoordinate - p3.yCoordinate) + 
        p2.xCoordinate * (p3.yCoordinate - p1.yCoordinate) + 
        p3.xCoordinate * (p1.yCoordinate - p2.yCoordinate)) / 2

def IsZeroArea(p1, p2, p3):
    return ComputeArea(p1, p2, p3) == 0

def ComputeLength(p1, p2):
    return ((p1.xCoordinate - p2.xCoordinate) ** 2 + (p1.yCoordinate - p2.yCoordinate) ** 2) ** 0.5
    
def ComputeLengthType(d1, d2, d3):
    if (IsAlmostEqual(d1, d2, 7) or IsAlmostEqual(d1, d3, 7) or IsAlmostEqual(d2, d3, 7)): return "isosceles"
    else: return "scalene"
    
def ComputeAngle(adjD1, adjD2, oppD):
    return acos((adjD1 ** 2 + adjD2 ** 2 - oppD ** 2) / (2 * adjD1 * adjD2))
    
def HasZeroAngle(a1, a2, a3):
    return IsAlmostEqual(a1, 0, 7) or IsAlmostEqual(a2, 0, 7) or IsAlmostEqual(a3, 0, 7)
    
def HasOverPiAngle(a1, a2, a3):
    return (a1 > pi) or (a2 > pi) or (a3 > pi)
    
def ComputeAngleType(a1, a2, a3): 
    if (IsAlmostEqual(a1, pi / 2, 7) or IsAlmostEqual(a2, pi / 2, 7) or IsAlmostEqual(a3, pi / 2, 7)): return "right"
    elif ((a1 > pi / 2) or (a2 > pi / 2) or (a3 > pi / 2)): return "obtuse"
    else: return "acute" 
    
def IsAlmostEqual(f1, f2, digit):
    return abs(f1 - f2) < 0.1 ** digit
    
def PrintAllResults():
    InitializeInputTestCases()
    for x in range(len(inputTestCases)):
        result = inputTestCases[x].ComputeResult()
        print("Case #" + str(x + 1) + ": " + result)
        
PrintAllResults()
