# Import files
import lireLaby
import fonctions
import navigation
import turtle
import tkinter as tk
import buttons

# # # # # #  PRIMARY PROGRAM  # # # # # #

#### INITIALISATION ####
fonctions.askFIle()

# Question 1 : print matrix + entrance + exit
fonctions.display_matrix()

# # Question 2: Graphic display of the maz
laby = lireLaby.gameDict['laby']
fonctions.textDisplay(laby)

fonctions.askSide()
fonctions.graphicDisplay(laby)

# Appel de la fonction
fonctions.pixel2cell()

# turtle.up()
# turtle.goto(fonctions.cell2pixel(0, 10))

# line = 0 #int(input("line : "))
# column = 10 #int(input("column : "))
# print(fonctions.typeCellule(line, column))

fonctions.displayCrosses()  


# turtle.onscreenclick(fonctions.testClic)
# turtle.onscreenclick(fonctions.cell2pixel)
# turtle.onscreenclick(fonctions.buttonClick)

# pour laby 1:
counting_movements = ['r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'l', 'l', 'l', 'l', 'l', 'l', 'l', 'l', 'l', 'u', 'u', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r']
restart = tk.Button(tk.Tk(), text ="Restart", fg = "black", command = buttons.reintialisation)
restart.pack(side = 'bottom')

# exit = tk.Button(tk.Tk(), text ="exit", fg = "black", command = buttons.exit)
# exit.pack()

# automatic = tk.Button(tk.Tk(), text ="automatic exploration", fg = "black", command = buttons.launchAuto)
# automatic.pack()

# manual = tk.Button(tk.Tk(), text ="manual exploration", fg = "black", command = buttons.launchManual)
# manual.pack()

turtle.mainloop()


#navigation.movements()

#print(navigation.follow_path(counting_movements))
#print(navigation.inversePath(counting_movements))

navigation.explorer()


# screen.mainloop()
