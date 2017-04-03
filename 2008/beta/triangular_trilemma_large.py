# Google Code Jam
# Practice Contests
# Code Jam Beta 2008
# Problem A. Triangular Trilemma

# Solved

from math import pi
from math import acos

class Point:
    def __init__(self, x, y):
        self.x_coordinate = x
        self.y_coordinate = y
        
    def __eq__(self, other):
        return self.x_coordinate == other.x_coordinate and \
            self.y_coordinate == other.y_coordinate
        
class Triangle:
    def __init__(self, x1, y1, x2, y2, x3, y3):
        p1 = Point(x1, y1)
        p2 = Point(x2, y2)
        p3 = Point(x3, y3)
        self.point1 = p1
        self.point2 = p2
        self.point3 = p3
        
        is_seperated_points_ = is_seperated_points(self.point1, self.point2, self.point3)
        is_zero_area_ = is_zero_area(self.point1, self.point2, self.point3)
        if (is_seperated_points_ and not is_zero_area_): 
            self.length1 = compute_length(self.point1, self.point2)
            self.length2 = compute_length(self.point1, self.point3)
            self.length3 = compute_length(self.point2, self.point3)
            
            self.angle1 = compute_angle(self.length1, self.length2, self.length3)
            self.angle2 = compute_angle(self.length1, self.length3, self.length2)
            self.angle3 = compute_angle(self.length2, self.length3, self.length1)
            
    def compute_result(self):
        if (not is_seperated_points(self.point1, self.point2, self.point3)): return "not a triangle"
        elif (is_zero_area(self.point1, self.point2, self.point3)): return "not a triangle"
        elif (has_zero_angle(self.angle1, self.angle2, self.angle3)): return "not a triangle"
        elif (has_over_pi_angle(self.angle1, self.angle2, self.angle3)): return "not a triangle"
        else: 
            length_type = compute_length_type(self.length1, self.length2, self.length3)
            angle_type = compute_angle_type(self.angle1, self.angle2, self.angle3)
            return length_type + " " + angle_type + " triangle"
        
def initialize_test_cases(lines):
    global test_cases
    for index, item in enumerate(lines):
        if index > 0:  
            items = item.split(' ')
            if (len(items) > 1): 
                x1 = int(items[0])
                y1 = int(items[1])
                x2 = int(items[2])
                y2 = int(items[3])
                x3 = int(items[4])
                y3 = int(items[5])
                test_cases[index - 1] = Triangle(x1, y1, x2, y2, x3, y3)

def is_seperated_points(p1, p2, p3):
    if ((p1 == p2) or (p1 == p3) or (p2 == p3)): return False
    else: return True
    
def compute_area(p1, p2, p3):
    return (p1.x_coordinate * (p2.y_coordinate - p3.y_coordinate) + 
        p2.x_coordinate * (p3.y_coordinate - p1.y_coordinate) + 
        p3.x_coordinate * (p1.y_coordinate - p2.y_coordinate)) / 2

def is_zero_area(p1, p2, p3):
    return compute_area(p1, p2, p3) == 0

def compute_length(p1, p2):
    return ((p1.x_coordinate - p2.x_coordinate) ** 2 + (p1.y_coordinate - p2.y_coordinate) ** 2) ** 0.5
    
def compute_length_type(d1, d2, d3):
    if (is_almost_equal(d1, d2, 7) or is_almost_equal(d1, d3, 7) or is_almost_equal(d2, d3, 7)): return "isosceles"
    else: return "scalene"
    
def compute_angle(adj_d1, adj_d2, opp_d):
    return acos((adj_d1 ** 2 + adj_d2 ** 2 - opp_d ** 2) / (2 * adj_d1 * adj_d2))
    
def has_zero_angle(a1, a2, a3):
    return is_almost_equal(a1, 0, 7) or is_almost_equal(a2, 0, 7) or is_almost_equal(a3, 0, 7)
    
def has_over_pi_angle(a1, a2, a3):
    return (a1 > pi) or (a2 > pi) or (a3 > pi)
    
def compute_angle_type(a1, a2, a3): 
    if (is_almost_equal(a1, pi / 2, 7) or is_almost_equal(a2, pi / 2, 7) or is_almost_equal(a3, pi / 2, 7)): return "right"
    elif ((a1 > pi / 2) or (a2 > pi / 2) or (a3 > pi / 2)): return "obtuse"
    else: return "acute" 
    
def is_almost_equal(f1, f2, digit):
    return abs(f1 - f2) < 0.1 ** digit
    
def print_all_results():
    for x in range(len(test_cases)):
        result = test_cases[x].compute_result()
        print("Case #" + str(x + 1) + ": " + result)

test_case_file = open("TriangularTrilemma_A-large-practice.in", "r")
lines = test_case_file.read().split('\n')
n = int(lines[0])
test_cases = [0 for x in range(n)]
initialize_test_cases(lines)
print_all_results()
