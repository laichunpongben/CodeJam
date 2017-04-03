# Google Code Jam
# Practice Contests
# Practice Contest
# Problem B. Square Fields

# Unsolved

test_cases = [0 for x in range(9)]

class TestCase:
    def __init__(self, n, k):
        self.point_count = n
        self.square_count = k
        self.points = [0 for x in range(n)]
        
    def can_square_length_cover_all_points(self, square_length):
        for point_list in choose_iter(self.points, self.square_count):
            for point in point_list:
                create_square(point, square_length, 0)
        
        for x in range(self.square_count):
            check_if_point_covered = 0
            
            for point in range(self.points):
                if True: check_if_point_covered += 1
        
    def compute_min_square_length(self):
        check_if_point_covered = 0
        while (check_if_point_covered < self.point_count):
            return 0

class Point:
    def __init__(self, x, y):
        self.x_coordinate = x
        self.y_coordinate = y
        
class Square:
    def __init__(self, p1, p2):
        self.point_left_top = p1
        self.point_bottom_right = p2

def initialize_test_cases():
    global test_cases
    
    test_cases[0] = TestCase(7, 3)
    test_cases[0].points[0] = Point(57662, 11098)
    test_cases[0].points[1] = Point(7433, 12634)
    test_cases[0].points[2] = Point(48045, 56219)
    test_cases[0].points[3] = Point(1366, 25537)
    test_cases[0].points[4] = Point(6090, 15595)
    test_cases[0].points[5] = Point(13249, 38816)
    test_cases[0].points[6] = Point(21017, 10819)
    
    test_cases[1] = TestCase(7, 6)
    test_cases[1].points[0] = Point(45478, 25234)
    test_cases[1].points[1] = Point(15535, 30676)
    test_cases[1].points[2] = Point(24296, 47028)
    test_cases[1].points[3] = Point(18199, 28596)
    test_cases[1].points[4] = Point(35003, 54487)
    test_cases[1].points[5] = Point(30281, 16910)
    test_cases[1].points[6] = Point(45349, 37102)

    test_cases[2] = TestCase(7, 4)
    test_cases[2].points[0] = Point(1690, 845)
    test_cases[2].points[1] = Point(1690, 0)
    test_cases[2].points[2] = Point(0, 1690)
    test_cases[2].points[3] = Point(845, 1690)
    test_cases[2].points[4] = Point(1690, 2535)
    test_cases[2].points[5] = Point(1690, 3380)
    test_cases[2].points[6] = Point(2535, 1690)

    test_cases[3] = TestCase(3, 2)
    test_cases[3].points[0] = Point(3, 3)
    test_cases[3].points[1] = Point(3, 6)
    test_cases[3].points[2] = Point(6, 9)

    test_cases[4] = TestCase(7, 3)
    test_cases[4].points[0] = Point(2737, 1694)
    test_cases[4].points[1] = Point(1365, 1067)
    test_cases[4].points[2] = Point(1989, 2247)
    test_cases[4].points[3] = Point(2281, 2624)
    test_cases[4].points[4] = Point(1995, 3247)
    test_cases[4].points[5] = Point(3641, 1106)
    test_cases[4].points[6] = Point(2372, 2566)

    test_cases[5] = TestCase(7, 2)
    test_cases[5].points[0] = Point(76, 89)
    test_cases[5].points[1] = Point(44, 88)
    test_cases[5].points[2] = Point(82, 51)
    test_cases[5].points[3] = Point(45, 82)
    test_cases[5].points[4] = Point(57, 101)
    test_cases[5].points[5] = Point(69, 56)
    test_cases[5].points[6] = Point(98, 80)

    test_cases[6] = TestCase(7, 6)
    test_cases[6].points[0] = Point(2714, 34432)
    test_cases[6].points[1] = Point(54601, 32052)
    test_cases[6].points[2] = Point(40836, 1601)
    test_cases[6].points[3] = Point(38100, 36380)
    test_cases[6].points[4] = Point(34557, 23472)
    test_cases[6].points[5] = Point(22208, 58831)
    test_cases[6].points[6] = Point(2183, 1298)

    test_cases[7] = TestCase(5, 2)
    test_cases[7].points[0] = Point(1, 1)
    test_cases[7].points[1] = Point(2, 2)
    test_cases[7].points[2] = Point(3, 3)
    test_cases[7].points[3] = Point(6, 6)
    test_cases[7].points[4] = Point(7, 8)

    test_cases[8] = TestCase(4, 2)
    test_cases[8].points[0] = Point(864, 25548)
    test_cases[8].points[1] = Point(23328, 12075)
    test_cases[8].points[2] = Point(22093, 26174)
    test_cases[8].points[3] = Point(10708, 39349)

def create_square(point, length, direction):
    p1 = 0
    p2 = 0
    if (direction == 0):
        p1 = Point(point.x_coordinate, point.y_coordinate + length)
        p2 = Point(point.x_coordinate + length, point.y_coordinate)
    if (direction == 1):
        p1 = point
        p2 = Point(point.x_coordinate + length, point.y_coordinate - length)
    if (direction == 2):
        p1 = Point(point.x_coordinate - length, point.y_coordinate)
        p2 = Point(point.x_coordinate, point.y_coordinate - length)
    if (direction == 3):
        p1 = Point(point.x_coordinate - length, point.y_coordinate + length)
        p2 = point
    return Square(p1, p2)

def is_point_in_square(point, square):
    return (square.point_left_top.x_coordinate <= point.x_coordinate) and \
    (point.x_coordinate <= square.point_bottom_right.x_coordinate) and \
    (square.point_left_top.y_coordinate <= point.y_coordinate) and \
    (point.y_coordinate <= square.point_bottom_right.y_coordinate)
    
def choose_iter(elements, length):
    for i in xrange(len(elements)):
        if length == 1:
            yield (elements[i],)
        else:
            for next in choose_iter(elements[i+1:len(elements)], length-1):
                yield (elements[i],) + next
                
def choose(n, k):
    return list(choose_iter(n, k))
    
def print_all_results():
    pass
    
initialize_test_cases()
print_all_results()
