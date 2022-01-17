# By
#  ________    ___   ________   ________   ___        ________     
# |\   ___  \ |\  \ |\   ____\ |\   __  \ |\  \      |\   __  \    
# \ \  \\ \  \\ \  \\ \  \___| \ \  \|\  \\ \  \     \ \  \|\  \   
#  \ \  \\ \  \\ \  \\ \  \     \ \  \\\  \\ \  \     \ \   __  \  
#   \ \  \\ \  \\ \  \\ \  \____ \ \  \\\  \\ \  \____ \ \  \ \  \ 
#    \ \__\\ \__\\ \__\\ \_______\\ \_______\\ \_______\\ \__\ \__\
#     \|__| \|__| \|__| \|_______| \|_______| \|_______| \|__|\|__|
                                                                 
                                                                 
                                                                 
class Shape:
    green = 0
    blue = 0
    red = 0
    avg_area = 0

    def __init__(self, number, color):
        self.number = number
        self.color = color

    def calc_area(self):
        pass

    @classmethod
    def color_counter(cls, color1):
        if color1 == 'Blue':
            cls.blue += 1
        elif color1 == 'Red':
            cls.red += 1
        elif color1 == 'Green':
            cls.green += 1


class Circle(Shape):
    def __init__(self, number, color, measure):
        super().__init__(number, color)
        self.measure = measure

    @property
    def calc_area(self):
        return float((self.measure ** 2) * 3.1415)

    def __str__(self):
        return 'Circle({}, {}, {})'.format(self.number, self.color, self.measure)


class Square(Shape):
    def __init__(self, number, color, measure):
        super().__init__(number, color)
        self.measure = measure

    @property
    def calc_area(self):
        return float(self.measure ** 2)

    def __str__(self):
        return 'Square( {}, {}, {} )'.format(self.number, self.color, self.measure)


CircleList = []
SquareList = []

try:
    f = open("Shapes.txt")
    for line in f:
        ShapeType, Number, Color, Measur = line.split(';')
        if ShapeType == "Circle":
            CircleList.append(Circle(int(Number), Color, float(Measur)))
            Circle.color_counter(Color)
        elif ShapeType == "Square":
            SquareList.append(Square(int(Number), Color, float(Measur)))
            Square.color_counter(Color)

except FileNotFoundError as e:
    print(e)


while True:
    print("""
    a. Print colors frequency for each Shape.
    b. Print the average area for each type. 
    c. Find and print details of shapes with min and max area for each type
    q. Quit
    """)
    choice = input('Enter Letter : ')
    if choice == 'a' or choice == 'A':
        print(
            f'Circle:{{Red:{Circle.red}, Green:{Circle.green}, Blue:{Circle.blue}}}')
        print(
            f'Square:{{Red:{Square.red}, Green:{Square.green}, Blue:{Square.blue}}}')
    elif choice == 'b' or choice == 'B':
        sumarea = 0
        for area in CircleList:
            sumarea += area.calc_area
        avgC = float( sumarea / len(CircleList))
        if avgC < 100:
            print('Circle: Circle Average below 100')
        else:
            print(f'Circle: Average area is {avgC}')
        
        sumarea = 0
        for area in SquareList:
            sumarea += area.calc_area
        avgS = float( sumarea / len(SquareList))
        if avgS < 100:
            print('Square: Square Average below 100')
        else:
            print(f'Square: Average area is {avgS}')

    elif choice == 'c' or choice == 'C':
        c = []
        for m in CircleList:
            c.append(m.measure)
        print(f'''Circle:\n\tMin area is {CircleList[c.index(min(c))].calc_area}, Circle ID: {min(c)}
        Max area is {CircleList[c.index(max(c))].calc_area}, Circle ID: {max(c)}
        ''')
        s = []
        for m in SquareList:
            s.append(m.measure)
        print(f'''Square:\n\tMin area is {SquareList[s.index(min(s))].calc_area}, Circle ID: {min(s)}
        Max area is {SquareList[s.index(max(s))].calc_area}, Square ID: {max(s)}
        ''')
    else:
        break
