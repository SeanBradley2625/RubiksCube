import copy
import readline
import random

class rubiksCube:
    def __init__(self, cube):
        self.cube = cube

    def __rotation(self, face, clockwise):
        copyFace = []
        if clockwise:
            faceIndex = (5,3,0,6,1,7,4,2)
        else:
            faceIndex = (2,4,7,1,6,0,3,5)
        for square in faceIndex:
            copyFace.append(face[square])
        return copyFace

    def __makeMove(self, move, cw):
        match move:
            case "up":
                sides = ((5,4), (2,5), (3,2), (4,3))
                indicies = (((0,1,2),(0,1,2)), ((0,1,2),(0,1,2)), ((0,1,2),(0,1,2)), ((0,1,2),(0,1,2)))
                rotationFace = 1
            case "down":
                sides = ((4,5), (5,2), (2,3), (3,4))
                indicies = (((5,6,7),(5,6,7)), ((5,6,7),(5,6,7)), ((5,6,7),(5,6,7)), ((5,6,7),(5,6,7)))
                rotationFace = 0
            case "left":
                sides = ((1,4), (4,0), (0,2), (2,1))
                indicies = (((0,3,5),(0,3,5)), ((0,3,5),(0,3,5)), ((0,3,5),(7,4,2)), ((7,4,2),(0,3,5)))
                rotationFace = 3
            case "right":
                sides = ((4,1), (0,4), (2,0), (1,2))
                indicies = (((2,4,7),(2,4,7)), ((2,4,7),(2,4,7)), ((5,3,0),(2,4,7)), ((2,4,7),(5,3,0)))
                rotationFace = 5
            case "front":
                sides = ((1,5), (5,0), (0,3), (3,1))
                indicies = (((5,6,7),(0,3,5)), ((0,3,5),(2,1,0)), ((2,1,0),(7,4,2)), ((7,4,2),(5,6,7)))
                rotationFace = 4
            case "back":
                sides = ((1,3), (3,0), (0,5), (5,1))
                indicies = (((0,1,2),(5,3,0)), ((5,3,0),(7,6,5)), ((7,6,5),(2,4,7)), ((2,4,7),(0,1,2)))
                rotationFace = 2
        if cw:
            sideVal = 1
        else:
            sideVal = 0
        copyCube = copy.deepcopy(self.cube)
        copyCube[rotationFace] = self.__rotation(copyCube[rotationFace], cw)
        for position in range(4):
            side = sides[position]
            index = indicies[position]
            for square in range(3):
                copyCube[side[sideVal]][index[sideVal][square]] = self.cube[side[not sideVal]][index[not sideVal][square]]
        self.cube = copyCube
    def up_cw(self):
        self.__makeMove("up",True)
    def up_ccw(self):
        self.__makeMove("up",False)
    def down_cw(self):
        self.__makeMove("down",True)
    def down_ccw(self):
        self.__makeMove("down",False)
    def left_cw(self):
        self.__makeMove("left",True)
    def left_ccw(self):
        self.__makeMove("left",False)
    def right_cw(self):
        self.__makeMove("right",True)
    def right_ccw(self):
        self.__makeMove("right",False)
    def front_cw(self):
        self.__makeMove("front",True)
    def front_ccw(self):
        self.__makeMove("front",False)
    def back_cw(self):
        self.__makeMove("back",True)
    def back_ccw(self):
        self.__makeMove("back",False)
    def listCube(self):
        return(self.cube)

def render(cube):
    print("                  ,-------,")
    print("                  |", cube[1][0], cube[1][1], cube[1][2], "|")
    print("                  |", cube[1][3], 1, cube[1][4], "|")
    print("                  |", cube[1][5], cube[1][6], cube[1][7], "|")
    print("  ,-------,-------o-------o-------,")
    print("  |", cube[2][0], cube[2][1], cube[2][2], "|", cube[3][0], cube[3][1], cube[3][2], "|", cube[4][0], cube[4][1], cube[4][2], "|", cube[5][0], cube[5][1], cube[5][2], "|")
    print("  |", cube[2][3], 2, cube[2][4], "|", cube[3][3], 3, cube[3][4], "|", cube[4][3], 4, cube[4][4], "|", cube[5][3], 5, cube[5][4], "|")
    print("  |", cube[2][5], cube[2][6], cube[2][7], "|", cube[3][5], cube[3][6], cube[3][7], "|", cube[4][5], cube[4][6], cube[4][7], "|", cube[5][5], cube[5][6], cube[5][7], "|")
    print("  '-------'-------o-------o-------'")
    print("                  |", cube[0][0], cube[0][1], cube[0][2], "|")
    print("                  |", cube[0][3], 0, cube[0][4], "|")
    print("                  |", cube[0][5], cube[0][6], cube[0][7], "|")
    print("                  '-------'")
    print("")

def makeMove(move):
    match move:
        case "up-cw":
            cube.up_cw()
        case "down-cw":
            cube.down_cw()
        case "left-cw":
            cube.left_cw()
        case "right-cw":
            cube.right_cw()
        case "front-cw":
            cube.front_cw()
        case "back-cw":
            cube.back_cw()
        case "up-ccw":
            cube.up_ccw()
        case "down-ccw":
            cube.down_ccw()
        case "left-ccw":
            cube.left_ccw()
        case "right-ccw":
            cube.right_ccw()
        case "front-ccw":
            cube.front_ccw()
        case "back-ccw":
            cube.back_ccw()
        case "scramble":
            for i in range(20):
                makeMove(posibleMoves[random.randint(0,11)])
        case "exit":
            print("Now exiting...")
            exit()
        case _:
            print("Invalid option!")
    return 0

cube = rubiksCube([[0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1],[2,2,2,2,2,2,2,2],[3,3,3,3,3,3,3,3],[4,4,4,4,4,4,4,4],[5,5,5,5,5,5,5,5]])
posibleMoves = ("up-cw", "down-cw", "left-cw", "right-cw", "front-cw", "back-cw", "up-ccw", "down-ccw", "left-ccw", "right-ccw", "front-ccw", "back-ccw")
print("\033c\n", end="")
render(cube.listCube())
while True:
    move = input("What move would you like to make? ")
    makeMove(move)
    render(cube.listCube())
