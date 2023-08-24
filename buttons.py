import turtle
import fonctions
import lireLaby
import navigation


def reintialisation ():
    turtle.color('yellow') # turtle default color is yellow
    x, y = fonctions.cell2pixelBIS(lireLaby.gameDict['entrance'][1], lireLaby.gameDict['entrance'][0])
    turtle.goto(x + lireLaby.gameDict['sidel']/2, y - lireLaby.gameDict['sideL']/2) # so turtle starts back at entrance for the guided navigation
    screen = turtle.Screen()
    turtle.bgpic('nopic')
    
def exit():
    turtle.bye()

def launchManual():
    navigation.movements
    turtle.mainloop()

def launchAuto():
    navigation.explorer
    