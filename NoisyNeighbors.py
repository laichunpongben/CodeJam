# Google Code Jam
# Google Code Jam 2015
# Round 1B
# Problem B. Noisy Neighbors

testCaseFile = open("NoisyNeighbors_B-small-practice.in", "r")
lines = testCaseFile.read().split('\n')
n = int(lines[0])
testCases = [0 for x in range(n)]

#apartments = [[[-1 for x in range(101)] for y in range(11)] for z in range(11)]
apartments = 0

class TestCase:
    def __init__(self, r, c, n):
        self.row = r
        self.column = c
        self.tenant = n
        
class Apartment:
    def __init__(self, r, c, n):
        self.row = r
        self.column = c
        self.tenant = n
        self.minUnhappiness = -1
        self.rowBorder = -1
        self.columnBorder = -1
        self.subApartments = []

def initialize_test_cases(lines):
    global testCases
    for index, item in enumerate(lines):
        if index > 0:  
            items = item.split(' ')
            if (len(items) > 1): 
                r = int(items[0])
                c = int(items[1])
                tenant = int(items[2])
                testCases[index - 1] = TestCase(r, c, tenant)

def initialize_apartments_tablebase():
    initialize_apartments()
    initialize_apartments_small_size_unhappiness()
    initialize_apartments_small_size_borders()
    initialize_apartments_recursively()
    
def initialize_apartments():
    global apartments
    apartments = [[[Apartment(r, c, n) for n in range(101)] for c in range(11)] for r in range(11)]
    
def initialize_apartments_small_size_unhappiness():
    global apartments
    apartments[1][1][0].minUnhappiness = 0
    apartments[1][1][1].minUnhappiness = 0
    apartments[2][1][0].minUnhappiness = 0
    apartments[2][1][1].minUnhappiness = 0
    apartments[2][1][2].minUnhappiness = 1
    apartments[1][2][0].minUnhappiness = 0
    apartments[1][2][1].minUnhappiness = 0
    apartments[1][2][2].minUnhappiness = 1
    apartments[2][2][0].minUnhappiness = 0
    apartments[2][2][1].minUnhappiness = 0
    apartments[2][2][2].minUnhappiness = 0
    apartments[2][2][3].minUnhappiness = 2
    apartments[2][2][4].minUnhappiness = 4
    
def initialize_apartments_small_size_borders():
    global apartments
    apartments[1][1][0].rowBorder= 0
    apartments[1][1][1].rowBorder = 1
    apartments[2][1][0].rowBorder = 0
    apartments[2][1][1].rowBorder = 1
    apartments[2][1][2].rowBorder = 2
    apartments[1][2][0].rowBorder = 0
    apartments[1][2][1].rowBorder = 0
    apartments[1][2][2].rowBorder = 1
    apartments[2][2][0].rowBorder = 0
    apartments[2][2][1].rowBorder = 0
    apartments[2][2][2].rowBorder = 1
    apartments[2][2][3].rowBorder = 1
    apartments[2][2][4].rowBorder = 2
    
    apartments[1][1][0].columnBorder= 0
    apartments[1][1][1].columnBorder = 1
    apartments[2][1][0].columnBorder = 0
    apartments[2][1][1].columnBorder = 0
    apartments[2][1][2].columnBorder = 1
    apartments[1][2][0].columnBorder = 0
    apartments[1][2][1].columnBorder = 1
    apartments[1][2][2].columnBorder = 2
    apartments[2][2][0].columnBorder = 0
    apartments[2][2][1].columnBorder = 0
    apartments[2][2][2].columnBorder = 1
    apartments[2][2][3].columnBorder = 1
    apartments[2][2][4].columnBorder = 2
    
def initialize_apartments_recursively():
    global apartments
    for r in range(1, 5):
        for c in range(1, 5):
            for n in range(0, r * c + 1):
                print('Apartment:' + str(r) + ',' + str(c) +',' + str(n))
                #minUnhappiness = apartments[r][c][n]
                #print(str(r) + ',' + str(c) + ',' + str(n) + ',' + str(minUnhappiness))
                if (apartments[r][c][n].minUnhappiness > -1): continue
                else: 
                    apartment = apartments[r][c][n]
                    apartments[r][c][n].subApartments = divide_apartment(apartment, 0)
                    apartments[r][c][n].minUnhappiness = compute_min_unhappiness(apartment)
                    apartments[r][c][n].rowBorder = compute_row_border(apartment)
                    apartments[r][c][n].columnBorder = compute_column_border(apartment)
                    
                    tempApartment = apartments[r][c][n]
                    tempApartment.subApartments = divide_apartment(tempApartment, 1)
                    tempApartment.minUnhappiness = compute_min_unhappiness(tempApartment)
                    tempApartment.rowBorder = compute_row_border(tempApartment)
                    tempApartment.columnBorder = compute_column_border(tempApartment)
                    
                    if (tempApartment.minUnhappiness < apartments[r][c][n].minUnhappiness):
                        apartments[r][c][n] = tempApartment
                    
def divide_apartment(apartment, tenantDifference):
    r = apartment.row
    c = apartment.column
    n = apartment.tenant
    
    r1 = r // 2
    r2 = r - r1
    c1 = c // 2
    c2 = c - c1
    n1 = n // 2
    n2 = n - n1
    
    if (r > 2 and c == 1): 
         c1 = 1
         c2 = 1
    elif (r == 1 and c > 2):
        r1 = 1
        r2 = 1
    elif (r > 1 and c > 1 and r > c): 
        c1 = c
        c2 = c
    elif (r > 1 and c > 1 and r <= c): 
        r1 = r
        r2 = r
    
    while (n1 == n2 and n1 > 0 and n2 > 0 and tenantDifference == 1):
        if (n1 <= n2): 
            n1 += -1
            n2 += 1
            #print(n1)
            #print(n2)
        else: 
            n1 += 1
            n2 += -1
            #print(n1)
            #print(n2)
    
    while (r1 * c1 < n1): 
        n1 += -1
        n2 += 1
        #print(n1)
        
    while (r2 * c2 < n2):
        n1 += 1
        n2 += -1
        #print(n2)
    
    apartment1 = apartments[r1][c1][n1]
    apartment2 = apartments[r2][c2][n2]
    subApartments = [apartment1, apartment2]
    #print('n1:' + str(apartment1.tenant))
    #print('n2:' + str(apartment2.tenant))
    
    return subApartments

def compute_min_unhappiness(apartment):
    r = apartment.row
    c = apartment.column
    n = apartment.tenant
    #print(n)
    
    if (len(apartment.subApartments) == 0): return apartments[r][c][n].minUnhappiness
    elif (r * c == n): return (r - 1) * c + (c - 1) * r
    else: 
        apartment1 = apartment.subApartments[0]
        apartment2 = apartment.subApartments[1]
        #print('n1:' + str(apartment1.tenant))
        #print('n2:' + str(apartment2.tenant))
        minUnhappiness1 = compute_min_unhappiness(apartment1)
        minUnhappiness2 = compute_min_unhappiness(apartment2)
        insideUnhappiness = compute_shared_border_unhappiness(apartment)
        #print(insideUnhappiness)
        minUnhappiness = minUnhappiness1 + minUnhappiness2 + insideUnhappiness
        
        stringConcat = [r, c, n, minUnhappiness, apartment1.row, apartment1.column, apartment1.tenant, apartment1.minUnhappiness, 
        apartment2.row, apartment2.column, apartment2.tenant, apartment2.minUnhappiness]
        #print(''.join(str(stringConcat)))
        print(stringConcat)
        return minUnhappiness

def compute_row_border(apartment):
    r = apartment.row
    c = apartment.column
    n = apartment.tenant
    
    if (len(apartment.subApartments) == 0): return apartments[r][c][n].rowBorder
    else: 
        apartment1 = apartment.subApartments[0]
        apartment2 = apartment.subApartments[1]
        rb1 = apartment1.rowBorder
        rb2 = apartment2.rowBorder
        print('rb1:' + str(rb1))
        print('rb2:' + str(rb2))
        if (r > c): return rb1 + rb2
        elif (r <= c): return int(min(rb1, rb2))
        else: return 0
    
def compute_column_border(apartment):
    r = apartment.row
    c = apartment.column
    n = apartment.tenant
    
    if (len(apartment.subApartments) == 0): return apartments[r][c][n].columnBorder
    else: 
        apartment1 = apartment.subApartments[0]
        apartment2 = apartment.subApartments[1]
        cb1 = apartment1.columnBorder
        cb2 = apartment2.columnBorder
        print('cb1:' + str(cb1))
        print('cb2:' + str(cb2))
        if (r > c): return int(min(cb1, cb2))
        elif (r <= c): return cb1 + cb2
        else: return 0

def compute_shared_border_unhappiness(apartment): 
    r = apartment.row
    c = apartment.column
    apartment1 = apartment.subApartments[0]
    apartment2 = apartment.subApartments[1]
    
    r1 = apartment1.row
    r2 = apartment2.row
    c1 = apartment1.column
    c2 = apartment2.column
    
    #print('r:' + str(r))
    #print('c:' + str(c))
    if (r > c): 
        cb1 = apartment1.columnBorder
        cb2 = apartment2.columnBorder
        #print(apartment1.minUnhappiness)
        #print(apartment2.minUnhappiness)
        #print(cb1)
        #print(cb2)
        return int(max(cb1 + cb2 - c1, 0))
    elif (r <= c):
        rb1 = apartment1.rowBorder
        rb2 = apartment2.rowBorder
        #print(apartment1.minUnhappiness)
        #print(apartment2.minUnhappiness)
        #print(rb1)
        #print(rb2)
        return int(max(rb1 + rb2 - r1, 0))

def print_all_apartment_sizes():
    for r in range(1, 5):
        for c in range(1, 5):
            for n in range(0, r * c + 1):
                minUnhappiness = apartments[r][c][n]
                print(str(r) + ',' + str(c) + ',' + str(n) + ',' + str(minUnhappiness))
    
#initialize_test_cases(lines)
initialize_apartments_tablebase()
#print_all_apartment_sizes()

#print(apartments[2][3][5])
