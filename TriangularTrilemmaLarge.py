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
    
    inputTestCases[0] = Triangle(-95, -31, -8, 40, -269, -173)
    inputTestCases[1] = Triangle(-772, -55, 73, 909, 647, 867)
    inputTestCases[2] = Triangle(17, 125, -21, -72, -180, 87)
    inputTestCases[3] = Triangle(92, -196, 93, -147, 142, -146)
    inputTestCases[4] = Triangle(70, 70, 228, 255, -115, -88)
    inputTestCases[5] = Triangle(-346, 397, 698, -485, -479, -221)
    inputTestCases[6] = Triangle(-713, -640, 760, 849, 828, 394)
    inputTestCases[7] = Triangle(-255, 185, -29, 77, -142, 131)
    inputTestCases[8] = Triangle(130, -25, 185, -133, 22, 30)
    inputTestCases[9] = Triangle(405, -34, 419, -945, -726, -473)
    inputTestCases[10] = Triangle(-37, -49, 75, -98, -37, -147)
    inputTestCases[11] = Triangle(76, -130, 28, -292, 100, -49)
    inputTestCases[12] = Triangle(-145, 110, 53, -16, 251, 110)
    inputTestCases[13] = Triangle(565, -126, 22, 123, 31, -144)
    inputTestCases[14] = Triangle(-947, 575, -275, 395, -391, 518)
    inputTestCases[15] = Triangle(201, -251, 55, -91, 135, -18)
    inputTestCases[16] = Triangle(348, 407, -803, -848, -222, 298)
    inputTestCases[17] = Triangle(10, -84, -72, 37, 10, 158)
    inputTestCases[18] = Triangle(-66, 101, -22, -42, 121, 2)
    inputTestCases[19] = Triangle(-98, -111, 1, 39, 1, 39)
    inputTestCases[20] = Triangle(93, 53, -38, -50, 79, -64)
    inputTestCases[21] = Triangle(-103, 71, -203, -489, 101, -81)
    inputTestCases[22] = Triangle(-512, 809, 405, -713, -817, -400)
    inputTestCases[23] = Triangle(83, 142, 22, -104, 22, 388)
    inputTestCases[24] = Triangle(-25, -36, -39, 24, -85, -22)
    inputTestCases[25] = Triangle(623, -33, 125, -63, 115, 103)
    inputTestCases[26] = Triangle(207, -428, -103, -126, 48, 29)
    inputTestCases[27] = Triangle(829, -38, 926, -590, -53, 339)
    inputTestCases[28] = Triangle(71, 178, 71, -136, -13, 21)
    inputTestCases[29] = Triangle(-93, -148, 257, -282, 149, -40)
    inputTestCases[30] = Triangle(-98, -117, -122, -67, -85, -80)
    inputTestCases[31] = Triangle(-68, -78, -279, -247, 143, 91)
    inputTestCases[32] = Triangle(-399, 231, 308, -231, -983, 900)
    inputTestCases[33] = Triangle(-583, 844, -131, -636, -617, 461)
    inputTestCases[34] = Triangle(-107, 67, 100, -61, -284, -682)
    inputTestCases[35] = Triangle(8, -39, -2, -39, 3, -16)
    inputTestCases[36] = Triangle(-57, -19, -57, -19, -57, -19)
    inputTestCases[37] = Triangle(-279, 242, -110, 54, 59, -134)
    inputTestCases[38] = Triangle(91, 29, -26, -63, -26, 121)
    inputTestCases[39] = Triangle(109, 158, 121, 790, -402, 403)
    inputTestCases[40] = Triangle(124, 73, -36, -84, -33, 233)
    inputTestCases[41] = Triangle(-144, 615, 628, -659, -924, -464)
    inputTestCases[42] = Triangle(-866, -470, -53, 440, 463, -227)
    inputTestCases[43] = Triangle(143, 83, 43, 217, 93, 150)
    inputTestCases[44] = Triangle(-58, -145, -149, -145, -149, -418)
    inputTestCases[45] = Triangle(-710, 681, 692, 178, -762, 652)
    inputTestCases[46] = Triangle(23, 6, -126, 75, -17, 115)
    inputTestCases[47] = Triangle(184, -285, -12, -48, 122, -17)
    inputTestCases[48] = Triangle(23, -51, 23, 109, -134, 29)
    inputTestCases[49] = Triangle(28, -100, 50, 70, -142, -122)
    inputTestCases[50] = Triangle(73, -22, -11, 70, 241, -206)
    inputTestCases[51] = Triangle(98, -94, 98, -94, 98, -94)
    inputTestCases[52] = Triangle(-164, -192, 145, -133, -39, -8)
    inputTestCases[53] = Triangle(244, -334, 163, -966, -754, 893)
    inputTestCases[54] = Triangle(-18, 63, 73, -13, -109, -13)
    inputTestCases[55] = Triangle(-102, -106, -33, -74, -134, -37)
    inputTestCases[56] = Triangle(19, -31, 19, -31, 19, -31)
    inputTestCases[57] = Triangle(-120, 81, -28, 194, -28, -32)
    inputTestCases[58] = Triangle(-877, 482, 68, -858, 949, -446)
    inputTestCases[59] = Triangle(147, -97, 252, -220, 24, 8)
    inputTestCases[60] = Triangle(217, -749, 297, -221, -336, -300)
    inputTestCases[61] = Triangle(233, -16, -810, 634, 888, 725)
    inputTestCases[62] = Triangle(145, 111, 24, 347, 24, -125)
    inputTestCases[63] = Triangle(773, -493, -640, 585, 237, 853)
    inputTestCases[64] = Triangle(-132, -186, 78, -132, -54, -54)
    inputTestCases[65] = Triangle(63, 1, 63, 1, 63, 1)
    inputTestCases[66] = Triangle(-234, 472, 677, -219, 888, 529)
    inputTestCases[67] = Triangle(-150, -40, -97, 24, -214, -93)
    inputTestCases[68] = Triangle(96, 61, 101, -9, 26, 66)
    inputTestCases[69] = Triangle(-1, -297, -120, -102, 37, -140)
    inputTestCases[70] = Triangle(-123, -49, -192, 56, -105, 38)
    inputTestCases[71] = Triangle(21, -104, -112, 30, 287, -372)
    inputTestCases[72] = Triangle(66, 55, 66, 55, 145, -55)
    inputTestCases[73] = Triangle(-7, -128, -24, -255, 120, -111)
    inputTestCases[74] = Triangle(15, 10, -14, 26, 2, -3)
    inputTestCases[75] = Triangle(342, -740, -629, -136, 3, 208)
    inputTestCases[76] = Triangle(-142, -139, -49, -248, -49, -30)
    inputTestCases[77] = Triangle(-343, 537, 774, 42, 754, -148)
    inputTestCases[78] = Triangle(-970, 67, -586, 885, -740, 807)
    inputTestCases[79] = Triangle(-826, -458, -477, -946, -755, 162)
    inputTestCases[80] = Triangle(-782, -985, 837, -252, 31, 902)
    inputTestCases[81] = Triangle(146, -9, 134, -9, 140, -69)
    inputTestCases[82] = Triangle(-123, 147, 116, -102, -362, -102)
    inputTestCases[83] = Triangle(-56, -192, -56, -86, -85, -139)
    inputTestCases[84] = Triangle(-279, 489, 758, -778, 692, -730)
    inputTestCases[85] = Triangle(-217, 60, -140, -77, -63, 60)
    inputTestCases[86] = Triangle(150, -46, 150, -46, 150, -46)
    inputTestCases[87] = Triangle(474, 705, -511, -679, 73, -333)
    inputTestCases[88] = Triangle(-113, 65, 347, 65, 117, -53)
    inputTestCases[89] = Triangle(15, 110, -33, 110, -33, 110)
    inputTestCases[90] = Triangle(145, 131, 28, 14, 27, 132)
    inputTestCases[91] = Triangle(0, 87, 5, -10, 15, -204)
    inputTestCases[92] = Triangle(-76, 3, -142, -109, -30, -175)
    inputTestCases[93] = Triangle(-95, -23, -103, -95, -111, -23)
    inputTestCases[94] = Triangle(-150, -101, 177, 226, -59, 135)
    inputTestCases[95] = Triangle(-123, 144, -385, 97, 139, 97)
    inputTestCases[96] = Triangle(-98, 39, -122, 32, -91, 15)
    inputTestCases[97] = Triangle(-180, 14, 58, 90, -61, 52)
    inputTestCases[98] = Triangle(-139, -16, -58, -20, -301, -8)
    inputTestCases[99] = Triangle(-20, -80, -27, 25, -6, -290)

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
