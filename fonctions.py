import lireLaby
import turtle
import random
import tkinter as tk
from tkinter import ttk

def star(): # defining the starts drawn as the bg
    size = random.randint(3, 10)
    turtle.color('white', 'white')
    turtle.begin_fill()
    for i in range (36):
        turtle.forward(size)
        turtle.left(170)
    turtle.end_fill()
    
def drawStar (): #drawing the star
    turtle.delay(0)
    turtle.bgcolor('black')
    for j in range (40):
        x = random.randint(-675, 600)
        y = random.randint(-300, 350)
        star()
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()

def askFIle(): # ask file function
    file_name = 'laby1.laby' #input("Which labyrinth file do you want ? (laby0/laby1) ")
    lireLaby.gameDict['file_name'] = file_name


# Display in a readable way the matrix
def display_matrix():
    laby, mazeIn, mazeOut = lireLaby.labyFromFile(lireLaby.gameDict['file_name'])
    long_laby = len(laby)
    
    for i in range(long_laby):
        print(laby[i])

    print("")
    print("Coordinates of entrance : ", mazeIn)
    print("")
    print("Coordinates of exit: ", mazeOut)
    print("")

    lireLaby.gameDict['laby'] = laby
    lireLaby.gameDict['entrance'] = mazeIn
    lireLaby.gameDict['exit'] = mazeOut


def askSide():
    sidel = 30 #int(input("length of pixel ? "))
    sideL = 30 #int(input("width of pixel ? "))
    lireLaby.gameDict['sidel'] = sidel
    lireLaby.gameDict['sideL'] = sideL


def textDisplay(laby):
    # Let's consider that the position can be X Y
    entranceX = lireLaby.gameDict["entrance"]; entranceY = lireLaby.gameDict["entrance"]; 
    exitX = lireLaby.gameDict["exit"]; exitY = lireLaby.gameDict["exit"]; 

    # n is the list number      # m is the position in the n list
    n = 0
    for i in range(len(laby)):
        m = 0
        for j in laby[n]:
            if n == entranceX and m == entranceY:
                print("x", end=" ")
            elif n == exitX and m == exitY:
                print("o", end=" ")
            else:
                if j == 1:
                    print("#", end=" ")
                elif j == 0:
                    print(" ", end=" ")
            m += 1
        n += 1
        print("")    


# function to draw a filled square
def square(col):
    turtle.fillcolor(col) # coloring the square
    turtle.begin_fill()
    for i in range (2):
        turtle.forward(lireLaby.gameDict['sidel'])
        turtle.right(90)
        turtle.forward(lireLaby.gameDict['sideL'])
        turtle.right(90)
    turtle.end_fill()
# returns nothing, just draws a square


def graphicDisplay (laby):
    
    screen = turtle.Screen()
    screen.title('Exploring a maze')
    drawStar()
    coordX = -250; coordY = 250
    lireLaby.gameDict['coordX'] = -250; lireLaby.gameDict['coordY'] = 250

    # defining the entrance and exit coordinates
    entranceX = lireLaby.gameDict["entrance"][0]; entranceY = lireLaby.gameDict["entrance"][1]; 
    exitX = lireLaby.gameDict["exit"][0]; exitY = lireLaby.gameDict["exit"][1]; 
    sidel = lireLaby.gameDict['sidel']
    sideL = lireLaby.gameDict['sideL']
    laby = lireLaby.gameDict['laby']

    turtle.up()
    turtle.goto(coordX, coordY)
    turtle.down()

    turtle.delay(0) # increases speed of the drawing
    
    n = 0  # n is the list number  # m is the position in list n
    
    for _ in range (len(lireLaby.gameDict['laby'])): # continues loop until all lists have been examined
        m = 0
        s = sidel
        for i in laby[n]: #for every number in the sublist
            if n == exitX and m == exitY: # if exit, then square is light green
                square("light green")
                turtle.up()
                turtle.goto(coordX + s, coordY) # goes to coordinates for the next square to be drawn
                turtle.down()
                s += sidel
            elif n == entranceX and m == entranceY: # if entrance, then square is orange
                square("pink")
                turtle.up()
                turtle.goto(coordX + s, coordY) # goes to coordinates for the next square to be drawn
                turtle.down()
                s += sidel
            elif i == 1: # if there's a wall, white square is drawn
                square("white")
                turtle.up()
                turtle.goto(coordX + s, coordY) # goes to coordinates for the next square to be drawn
                turtle.down()
                s += sidel
            elif i == 0: # if there's a path, no squares are drawn, left white
                turtle.up()
                turtle.goto(coordX + s, coordY) # goes to coordinates for the next square to be drawn
                turtle.down()
                s += sidel
    
            m += 1
        coordY -= sideL # goes down to the next line of the labyrinth when first sublist has been examined
        turtle.up()
        turtle.goto(coordX, coordY) # goes to the right coordinates
        turtle.down()
        n += 1


def pixel2cell():
    line = 0
    column = 0

    # Coordonnées de la tortue géniale
    lireLaby.gameDict['coord_start_turt'] = turtle.position()

    start_X = lireLaby.gameDict['coordX']; start_Y = lireLaby.gameDict['coordY']

    start_X_turt = lireLaby.gameDict['coord_start_turt'][0]; start_Y_tur = lireLaby.gameDict['coord_start_turt'][1]

    #On compte +1 ligne toutes les unité de longueur entré dans side l
    while start_X < lireLaby.gameDict['coord_start_turt'][0]:
        start_X += lireLaby.gameDict["sidel"]
        line += 1

    # Même chose pour la largueur 
    while start_Y > lireLaby.gameDict['coord_start_turt'][1]:
        start_Y -= lireLaby.gameDict["sideL"]
        column += 1
    
    
    #print(line, column-1)
    return line, column-1


def testClic(x, y):
    line = -1
    column = -1

    start_X = lireLaby.gameDict['entrance'][0]
    start_Y = lireLaby.gameDict['entrance'][1] 

    # Calcul de la position sur Y de la première case car X reste le même (-250)
    coord_start_X = lireLaby.gameDict['coordX']
    coord_start_Y = lireLaby.gameDict['coordY']
    
    #On compte +1 ligne toutes les unité de longueur entré dans side l
    while coord_start_X < x:
        coord_start_X += lireLaby.gameDict['sidel']
        line += 1

    # Même chose pour la largueur 
    while coord_start_Y > y:
        coord_start_Y -= lireLaby.gameDict['sideL']
        column += 1

    #Si le clic sort du laby >0 ou < à la largeur / hauteur max
    if (line < 0 or line > len(lireLaby.gameDict['laby'][0])-1) or (column < 0 or column > len(lireLaby.gameDict['laby'])-1):
        line = None; column = None
        #print("Error, out of the labyrinth range")
    
    #print(line, column)
    return line, column        


# Coordinate of the center of the cell with testClic
def cell2pixel(i, j):
    i, j = testClic(i, j)
    if i == None and j == None:
        coord_mid_X = None
        coord_mid_Y = None
    else :
        coord_mid_X = (lireLaby.gameDict['coordX'] + (i * (lireLaby.gameDict['sidel']/2))) + (lireLaby.gameDict['sidel'] / 2)
        coord_mid_Y = (lireLaby.gameDict['coordY'] - (j * (lireLaby.gameDict['sideL']/2))) - (lireLaby.gameDict['sideL'] / 2)

    #print(coord_mid_X, coord_mid_Y)
    return coord_mid_X, coord_mid_Y


def typeCellule(line, column):

    # defining the type of an unic cel
    def typeCelUnic(line, column):
        typeCel = lireLaby.gameDict['laby'][column][line]

        if line == lireLaby.gameDict['entrance'][1] and column == lireLaby.gameDict['entrance'][0]:
            typeCel = "entrance"
        elif line == lireLaby.gameDict['exit'][1] and column == lireLaby.gameDict['exit'][0]:
            typeCel = "exit"
        else:
            if typeCel == 1:
                typeCel = "wall"
            elif typeCel == 0:
                typeCel = "path"    
        return typeCel

    cas = typeCelUnic(line, column)

    #test if what happen after to define the type of the case
    if cas == "path":
        way = 0

    # Testing the column +1, column -1, line +1, line -1 for an overview
        line -= 1
        for _ in range(2):
            typeCel = typeCelUnic(line, column)
            if typeCel == "path" or typeCel == "entrance" or typeCel == "exit":
                way += 1
            line += 2

        line -=3
        column -= 1
        for _ in range(2):
            typeCel = typeCelUnic(line, column)
            if typeCel == "path" or typeCel == "entrance" or typeCel == "exit":
                way += 1
            column += 2
        
        if way == 1:
            way = "dead-end"
        elif way == 2:
            way = "standard path"
        elif way > 2:
            way = "crossing"
    elif cas == "entrance":
        way = "entrance"
    elif cas == "exit":
        way = "exit"
    else:
        way = None
    
    #print(way)
    return way  


def cell2pixelBIS(line, column): # useful function adjacent to cell2pixel
    coord_mid_X = (lireLaby.gameDict['coordX'] + (line * (lireLaby.gameDict['sidel'])))
    coord_mid_Y = (lireLaby.gameDict['coordY'] - (column * (lireLaby.gameDict['sideL'])))
    return coord_mid_X, coord_mid_Y

# Looks for crossing in all "laby"
def displayCrosses():
    for columnCount in range(len(lireLaby.gameDict['laby'])-1):
        for lineCount in range(len(lireLaby.gameDict['laby'][columnCount])-1):
            way = typeCellule(lineCount, columnCount)
            if way == "crossing":
                move = cell2pixelBIS(lineCount, columnCount)
                turtle.up()
                turtle.goto(move)
                turtle.down()
                square("purple")

    turtle.color('yellow') # turtle default color is yellow
    x, y = cell2pixelBIS(lireLaby.gameDict['entrance'][1], lireLaby.gameDict['entrance'][0])
    turtle.up()
    turtle.goto(x + lireLaby.gameDict['sidel']/2, y - lireLaby.gameDict['sideL']/2) # so turtle starts back at entrance for the guided navigation

# Define the cel type for a unic cel 
def typeCelUnic(line, column):
    if line > len(lireLaby.gameDict['laby'][0]) -1 or column > len(lireLaby.gameDict['laby'])-1:
        typeCel = None
    else:
        typeCel = lireLaby.gameDict['laby'][column][line]

        # To prevent if the line or column incoming is out of the labyrinth range
        if line < 0 or column < 0:
            typeCel = None
        elif line > len(lireLaby.gameDict['laby'][0]) -1 or column > len(lireLaby.gameDict['laby']) -1 :
            typeCel = None

        else:
            if line == lireLaby.gameDict['entrance'][1] and column == lireLaby.gameDict['entrance'][0]:
                typeCel = "entrance"
            elif line == lireLaby.gameDict['exit'][1] and column == lireLaby.gameDict['exit'][0]:
                typeCel = "exit"
            else:
                if typeCel == 1:
                    typeCel = "wall"
                elif typeCel == 0:
                    typeCel = "path"    
    return typeCel

# Block the turtle bettween walls or cell type None (out of the range)
def guidedExploration():
    line, column = pixel2cell()
    line -= 1 # adapt the line to the actual line
    end = False

    exit = lireLaby.labyFromFile(lireLaby.gameDict['file_name'])[2]
    left = True; right = True; top = True; bot = True
    caseLeft = typeCelUnic(line-1, column); caseRight = typeCelUnic(line+1, column); caseTop = typeCelUnic(line, column-1); caseBot = typeCelUnic(line, column+1)
    #print("gauche : {}    droite : {}   hat : {}   bas : {}".format(caseLeft, caseRight, caseTop, caseBot))
    if pixel2cell()[1] == exit[0] and pixel2cell()[0] == exit[1] + 1 :
        end = True
    if caseLeft == "wall" or caseLeft == None:
        left = False
    if caseRight == "wall" or caseRight == None:
        right = False
    if caseTop == "wall" or caseTop == None:
        top = False
    if caseBot == "wall" or caseBot == None:
        bot = False

    return left, right, top, bot, end

