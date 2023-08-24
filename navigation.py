import turtle 
import fonctions
import lireLaby
import random

def movements():
	left, right, top, bot, end = fonctions.guidedExploration() # calling function to be able to use return values
	counting_movements = [] # intialising list to count commands
	exit = lireLaby.labyFromFile(lireLaby.gameDict['file_name'])[2]

	def gauche():
		left = fonctions.guidedExploration()[0]
		end = fonctions.guidedExploration()[4]
		w = True
		if left != False:
			while turtle.heading() != 180: # while turtle not heading left already, orient left
				turtle.right(90)
			turtle.forward(lireLaby.gameDict['sidel']) #then move forward
		else:
			turtle.color('red') # if turtle tries to head into a wall, turn red and display explanitory message
			print("There is a wall")
			w = False
		if fonctions.pixel2cell()[1] == exit[0] and fonctions.pixel2cell()[0] == exit[1] + 1:
			turtle.bgpic('among.gif')
		checkCell(w) # check if the type cell turtle is on is crossing, dead-end or exit, if so change color
		counting_movements.append('l')
	
		
	def droite(): # same comments as on top, just for right command
		right = fonctions.guidedExploration()[1]
		w = True
		if right != False:
			while turtle.heading() != 0:
				turtle.right(90)
			turtle.forward(lireLaby.gameDict['sidel'])
		else:
			turtle.color('red')
			print("There is a wall")
			w = False
		if fonctions.pixel2cell()[1] == exit[0] and fonctions.pixel2cell()[0] == exit[1] + 1:
			turtle.bgpic('among.gif')
		checkCell(w)
		counting_movements.append('r')
		
			
	def haut(): # same comments as on top, just for up command
		top = fonctions.guidedExploration()[2]
		end = fonctions.guidedExploration()[4]
		w = True
		if top != False:
			while turtle.heading() != 90:
				turtle.right(90)
			turtle.forward(lireLaby.gameDict['sideL'])
		else:
			turtle.color('red')
			print("There is a wall")
			w = False
		if fonctions.pixel2cell()[1] == exit[0] and fonctions.pixel2cell()[0] == exit[1] + 1:
			turtle.bgpic('among.gif')
		checkCell(w)
		counting_movements.append('u')
			
	def bas(): # same comments as on top, just for down command
		bot = fonctions.guidedExploration()[3]
		end = fonctions.guidedExploration()[4]
		w = True
		if bot != False:
			while turtle.heading() != 270:
				turtle.right(90)
			turtle.forward(lireLaby.gameDict['sideL'])
		else:
			turtle.color('red')
			print("There is a wall")
			w = False
		if fonctions.pixel2cell()[1] == exit[0] and fonctions.pixel2cell()[0] == exit[1] + 1:
			turtle.bgpic('among.gif')
		checkCell(w)
		counting_movements.append('d')
	
	# key bindings

	turtle.onkeypress(gauche,"Left")
	turtle.onkeypress(droite,"Right")
	turtle.onkeypress(haut,"Up")
	turtle.onkeypress(bas,"Down")

	turtle.listen()
	# start loop
	turtle.mainloop()

	print(counting_movements)
	return counting_movements


def checkCell(w): # checking type cell and changing color
	line = fonctions.pixel2cell()[0] - 1; column = fonctions.pixel2cell()[1] 
	typecel = fonctions.typeCellule(line, column)

	if w == True:
		if typecel == "entrance":
			turtle.color('yellow')
		elif typecel == "dead-end":
			turtle.color('blue')
		elif typecel == "crossing":
			turtle.color('pink')
		elif typecel == "exit":
			turtle.color('green')
		elif typecel == "standard path":
			turtle.color('yellow')


def follow_path(counting_movements):
	turtle.delay(20)

	x, y = fonctions.cell2pixelBIS(lireLaby.gameDict['entrance'][1], lireLaby.gameDict['entrance'][0])
	turtle.up()
	turtle.goto(x + lireLaby.gameDict['sidel']/2, y - lireLaby.gameDict['sideL']/2) # to be placed on the entrance
	
	line, column = fonctions.pixel2cell()
	typecel = fonctions.typeCelUnic(line, column) 
	exit = lireLaby.labyFromFile(lireLaby.gameDict['file_name'])[2] # defining exit cell 
	
	for move in range (len(counting_movements)): # traversing the list
		
		if typecel != "wall" and typecel != None: # if the cell is not a wall, i can move
			if counting_movements[move] == "r": # if right then i go right, if left then i go left, etc
				while turtle.heading() != 0:
					turtle.right(90)
				turtle.forward(lireLaby.gameDict['sidel'])
				line += 1
			elif counting_movements[move] == "l":
				while turtle.heading() != 180:
					turtle.right(90)
				turtle.forward(lireLaby.gameDict['sidel'])
				line -= 1
			elif counting_movements[move] == "d":
				while turtle.heading() != 270:
					turtle.right(90)
				turtle.forward(lireLaby.gameDict['sideL'])
				column -= 1
			elif counting_movements[move] == "u":
				while turtle.heading() != 90:
					turtle.right(90)
				turtle.forward(lireLaby.gameDict['sideL'])
				column += 1
			else:
				return counting_movements[move] + " is not a valid command" # if the command is not right, left, up or down
		else:
			return "There is a wall to the " + counting_movements[move] 
	
	if fonctions.pixel2cell()[1] == exit[0] and fonctions.pixel2cell()[0] == exit[1] + 1:
		turtle.bgpic('among.gif') # end picture
		

	turtle.mainloop()
	return "Congratulations, you won ! "

	
def inversePath (counting_movements):
	turtle.delay(20)

	x, y = fonctions.cell2pixelBIS(lireLaby.gameDict['exit'][1], lireLaby.gameDict['exit'][0])
	turtle.up()
	turtle.goto(x + lireLaby.gameDict['sidel']/2, y - lireLaby.gameDict['sideL']/2) # so it goes to the exit in order to start the inverse path
	
	for move in range(len(counting_movements) - 1, 0, -1): # traversing the list from end to beginning
		if counting_movements[move] == "r": 
			while turtle.heading() != 180: # if the list command is right, then i want to go left
				turtle.right(90)
			turtle.forward(lireLaby.gameDict['sidel'])
		elif counting_movements[move] == "l": 
			while turtle.heading() != 0: # if the list command is left, then i want to go right
				turtle.right(90)
			turtle.forward(lireLaby.gameDict['sidel'])
		elif counting_movements[move] == "d":
			while turtle.heading() != 90: # if the list command is down, then i want to go up
				turtle.right(90)
			turtle.forward(lireLaby.gameDict['sideL'])
		elif counting_movements[move] == "u":
			while turtle.heading() != 270: # if the list command is up, then i want to go down
				turtle.right(90)
			turtle.forward(lireLaby.gameDict['sideL'])
		else:
			return counting_movements[move] + " is not a valid command" # if the command is not right, left, up or down
	
	
	return "The path has successfully been inversed"

def explorer():
	# Setup of the turtle position	
	turtle.delay(20)
	x, y = fonctions.cell2pixelBIS(lireLaby.gameDict['entrance'][1], lireLaby.gameDict['entrance'][0])
	turtle.up()
	turtle.goto(x + lireLaby.gameDict['sidel']/2, y -(lireLaby.gameDict['sideL'])/2) # to be placed on the entrance
	
	line, column = fonctions.pixel2cell()
	typecel = fonctions.typeCelUnic(line, column) # defining the type of cell i want to go on in order to know if i can go there or not

	exit = lireLaby.labyFromFile(lireLaby.gameDict['file_name'])[2]

	# Creation of the commands list to store movement information
	lireLaby.gameDict['commands'] = []
	commands = lireLaby.gameDict['commands']

	
	# While turtle not at the end
	while fonctions.pixel2cell()[1] != exit[0] or fonctions.pixel2cell()[0] != exit[1] + 1:
	
		actual_turtle_pos_X = fonctions.pixel2cell()[0]
		actual_turtle_pos_Y = fonctions.pixel2cell()[1]
		direction = turtle.heading()
		
		moveCount = 0
		choices = 0

		if direction == 0: #droite
			# while it is a standard path and not anything else 
			while (fonctions.typeCellule(actual_turtle_pos_X, actual_turtle_pos_Y) == "standard path") and (fonctions.typeCelUnic(actual_turtle_pos_X, actual_turtle_pos_Y) != "wall") and (fonctions.typeCellule(actual_turtle_pos_X-1, actual_turtle_pos_Y) != "crossing") and (fonctions.typeCellule(actual_turtle_pos_X, actual_turtle_pos_Y) != "dead-end") or (fonctions.typeCellule(actual_turtle_pos_X, actual_turtle_pos_Y) == "entrance"):
				turtle.forward(lireLaby.gameDict['sidel'])
				actual_turtle_pos_X, actual_turtle_pos_Y = fonctions.pixel2cell()
				moveCount += 1
			for _ in range(moveCount):	
				commands.append('a')
			left, right, top, bot, end = fonctions.guidedExploration()
			# If there is an angle, rotate to setup the next step
			if left == True and right == False and top == True and bot == False:
				turtle.right(270)
				commands.append('g')
			elif left == True and right == False and top == False and bot == True:
				turtle.right(90)
				commands.append('d')

			#If we are on a crossing (consider as a checkpoint)
			if fonctions.typeCellule(actual_turtle_pos_X-1, actual_turtle_pos_Y) == "crossing":
				commands.append('checkpoint')
				if top == True:
					choices += 1
				if right == True:
					choices += 1
				if bot == True:
					choices += 1
				commands.append(choices)
				# Let the random fonction decide wich way bettween thee choices 2 minimum to 3 maximum
				way = random.randint(1, choices)
				if way == 1:
					if top == True:
						commands.append('g')
						turtle.right(270)
						commands.append('a')
						turtle.forward(lireLaby.gameDict['sideL'])
					else:
						commands.append('a')
						turtle.forward(lireLaby.gameDict['sidel'])
				elif way == 2:
					if right == True:
						commands.append('a')
						turtle.forward(lireLaby.gameDict['sidel'])
					else:
						commands.append('d')
						turtle.right(90)
						commands.append('a')
						turtle.forward(lireLaby.gameDict['sideL'])
				elif way == 3:
					if bot == True:
						commands.append('d')
						turtle.right(90)
						commands.append('a')
						turtle.forward(lireLaby.gameDict['sideL'])
					else:
						commands.append('g')
						turtle.right(270)
						commands.append('a')
						turtle.forward(lireLaby.gameDict['sideL'])
			
			#if we are in a dead-end
			elif fonctions.typeCellule(actual_turtle_pos_X-1, actual_turtle_pos_Y) == "dead-end":
				count = 0
				indice = len(commands) - 1
				search = len(commands) - 1
				while commands[indice] != "checkpoint":
					indice -= 1
					count += 1
				# while not at the checkpoint :
				while commands[search] != "checkpoint":

					# Reverse all of previous movements to arrived at a checkpoint (crossing)
					if turtle.heading() == 0: #droite
						print("droit droite")
						if commands[search] == 'a':
							turtle.forward(-(lireLaby.gameDict['sidel']))
						elif commands[search] == 'd':
							turtle.right(90)
						elif commands[search] == 'g':
							turtle.right(270)

					elif turtle.heading() == 180: #gauche
						print("droit gauche")
						if commands[search] == 'a':
							turtle.forward(-(lireLaby.gameDict['sidel']))
						elif commands[search] == 'd':
							turtle.right(270)
						elif commands[search] == 'g':
							turtle.right(90)

					elif turtle.heading() == 90: #haut
						print("droit haut")
						if commands[search] == 'a':
							turtle.forward(-(lireLaby.gameDict['sideL']))
						elif commands[search] == 'd':
							turtle.right(270)
						elif commands[search] == 'g':
							turtle.right(90)

					elif turtle.heading() == 270: #bas
						print("droit bas")
						if commands[search] == 'a':
							turtle.forward(-(lireLaby.gameDict['sideL']))
						elif commands[search] == 'd':
							turtle.right(90)
						elif commands[search] == 'g':
							turtle.right(270)
					
					commands.pop()
					search -= 1

			# if turtle arrived at end :
			if fonctions.typeCelUnic(actual_turtle_pos_X, actual_turtle_pos_Y) == "exit":
				turtle.forward(lireLaby.gameDict['sideL'])
		
		# Same for left movements
		elif direction == 180: #gauche
			while (fonctions.typeCellule(actual_turtle_pos_X-1, actual_turtle_pos_Y) == "standard path") and (fonctions.typeCelUnic(actual_turtle_pos_X-2, actual_turtle_pos_Y) != "wall") and (fonctions.typeCellule(actual_turtle_pos_X-1, actual_turtle_pos_Y) != "crossing") and (fonctions.typeCellule(actual_turtle_pos_X-1, actual_turtle_pos_Y) != "dead-end"):
				turtle.forward(lireLaby.gameDict['sidel'])
				# commands.append['g']
				actual_turtle_pos_X, actual_turtle_pos_Y = fonctions.pixel2cell()
				moveCount += 1
			for _ in range(moveCount):	
				commands.append('a')
			left, right, top, bot, end = fonctions.guidedExploration()
			if left == False and right == True and top == True and bot == False:
				turtle.right(90)
				commands.append('d')
			elif left == False and right == True and top == False and bot == True:
				turtle.right(270)
				commands.append('g')

			if fonctions.typeCellule(actual_turtle_pos_X-1, actual_turtle_pos_Y) == "crossing":
				commands.append('checkpoint')
				if bot == True:
					choices += 1
				if left == True:
					choices += 1
				if top == True:
					choices += 1
				commands.append(choices)
				way = random.randint(1, choices)
				if way == 1:
					if bot == True:
						commands.append('g')
						turtle.right(270)
						commands.append('a')
						turtle.forward(lireLaby.gameDict['sideL'])
					else:
						commands.append('a')
						turtle.forward(lireLaby.gameDict['sidel'])
				elif way == 2:
					if left == True:
						commands.append('a')
						turtle.forward(lireLaby.gameDict['sidel'])
					else:
						commands.append('d')
						turtle.right(90)
						commands.append('a')
						turtle.forward(lireLaby.gameDict['sideL'])
				elif way == 3:
					if top == True:
						commands.append('d')
						turtle.right(90)
						commands.append('a')
						turtle.forward(lireLaby.gameDict['sideL'])
					else:
						commands.append('g')
						turtle.right(270)
						commands.append('a')
						turtle.forward(lireLaby.gameDict['sideL'])

			elif fonctions.typeCellule(actual_turtle_pos_X-1, actual_turtle_pos_Y) == "dead-end":
				count = 0
				indice = len(commands) - 1
				search = len(commands) - 1
				while commands[indice] != "checkpoint":
					indice -= 1
					count += 1
				while commands[search] != "checkpoint":

					if turtle.heading() == 0: #droite
						print("gauche droite")
						if commands[search] == 'a':
							turtle.forward(-(lireLaby.gameDict['sidel']))
						elif commands[search] == 'd':
							turtle.right(270)
						elif commands[search] == 'g':
							turtle.right(90)

					elif turtle.heading() == 180: #gauche
						print("gauche gauche")
						if commands[search] == 'a':
							turtle.forward(-(lireLaby.gameDict['sidel']))
						elif commands[search] == 'd':
							turtle.right(270)
						elif commands[search] == 'g':
							turtle.right(90)

					elif turtle.heading() == 90: #haut
						print("gauche haut")
						if commands[search] == 'a':
							turtle.forward(-(lireLaby.gameDict['sideL']))
						elif commands[search] == 'd':
							turtle.right(90)
						elif commands[search] == 'g':
							turtle.right(270)

					elif turtle.heading() == 270: #bas
						print("gauche bas")
						if commands[search] == 'a':
							turtle.forward(-(lireLaby.gameDict['sideL']))
						elif commands[search] == 'd':
							turtle.right(90)
						elif commands[search] == 'g':
							turtle.right(90)
					
					commands.pop()
					search -= 1

			if fonctions.typeCelUnic(actual_turtle_pos_X-2, actual_turtle_pos_Y) == "exit":
				turtle.forward(lireLaby.gameDict['sideL'])
			

		# Same for top movement
		elif direction == 90: #haut
			while (fonctions.typeCellule(actual_turtle_pos_X-1, actual_turtle_pos_Y) == "standard path") and (fonctions.typeCelUnic(actual_turtle_pos_X-1, actual_turtle_pos_Y-1) != "wall") and (fonctions.typeCellule(actual_turtle_pos_X-1, actual_turtle_pos_Y) != "crossing") and (fonctions.typeCellule(actual_turtle_pos_X-1, actual_turtle_pos_Y) != "dead-end"):
				turtle.forward(lireLaby.gameDict['sideL'])
				# commands.append['h']
				actual_turtle_pos_X, actual_turtle_pos_Y = fonctions.pixel2cell()		
				moveCount += 1
			for _ in range(moveCount):	
				commands.append('a')	
			left, right, top, bot, end = fonctions.guidedExploration()
			if left == False and right == True and top == False and bot == True:
				turtle.right(90)
				commands.append('d')
			elif left == True and right == False and top == False and bot == True:
				turtle.right(270)
				commands.append('g')

			if fonctions.typeCellule(actual_turtle_pos_X-1, actual_turtle_pos_Y) == "crossing":
				commands.append('checkpoint')
				if left == True:
					choices += 1
				if top == True:
					choices += 1
				if right == True:
					choices += 1
				commands.append(choices)
				way = random.randint(1, choices)
				if way == 1:
					if left == True:
						commands.append('g')
						turtle.right(270)
						commands.append('a')
						turtle.forward(lireLaby.gameDict['sidel'])
					else:
						commands.append('a')
						turtle.forward(lireLaby.gameDict['sideL'])
				elif way == 2:
					if top == True:
						commands.append('a')
						turtle.forward(lireLaby.gameDict['sideL'])
					else:
						commands.append('d')
						turtle.right(90)
						commands.append('a')
						turtle.forward(lireLaby.gameDict['sidel'])
				elif way == 3:
					if right == True:
						commands.append('d')
						turtle.right(90)
						commands.append('a')
						turtle.forward(lireLaby.gameDict['sidel'])
					else:
						commands.append('g')
						turtle.right(270)
						commands.append('a')
						turtle.forward(lireLaby.gameDict['sidel'])
			
			elif fonctions.typeCellule(actual_turtle_pos_X-1, actual_turtle_pos_Y) == "dead-end":
				count = 0
				indice = len(commands) - 1
				search = len(commands) - 1
				while commands[indice] != "checkpoint":
					indice -= 1
					count += 1
				while commands[search] != "checkpoint":

					if turtle.heading() == 0: #droite
						print("haut droite")
						if commands[search] == 'a':
							turtle.forward(-(lireLaby.gameDict['sidel']))
						elif commands[search] == 'd':
							turtle.right(90)
						elif commands[search] == 'g':
							turtle.right(270)

					elif turtle.heading() == 180: #gauche
						print("haut gauche")
						if commands[search] == 'a':
							turtle.forward(-(lireLaby.gameDict['sidel']))
						elif commands[search] == 'd':
							turtle.right(90)
						elif commands[search] == 'g':
							turtle.right(270)

					elif turtle.heading() == 90: #haut
						print("haut haut")
						if commands[search] == 'a':
							turtle.forward(-(lireLaby.gameDict['sideL']))
						elif commands[search] == 'd':
							turtle.right(270)
						elif commands[search] == 'g':
							turtle.right(90)

					elif turtle.heading() == 270: #bas
						print("haut bas")
						if commands[search] == 'a':
							turtle.forward(-(lireLaby.gameDict['sideL']))
						elif commands[search] == 'd':
							turtle.right(90)
						elif commands[search] == 'g':
							turtle.right(270)
					
					commands.pop()
					search -= 1

			if fonctions.typeCelUnic(actual_turtle_pos_X-1, actual_turtle_pos_Y-1) == "exit":
				turtle.forward(lireLaby.gameDict['sideL'])
	
		# Same for bot movement
		elif direction == 270: #bas
			while (fonctions.typeCellule(actual_turtle_pos_X-1, actual_turtle_pos_Y) == "standard path") and (fonctions.typeCelUnic(actual_turtle_pos_X-1, actual_turtle_pos_Y+1) != "wall") and (fonctions.typeCellule(actual_turtle_pos_X-1, actual_turtle_pos_Y) != "crossing") and (fonctions.typeCellule(actual_turtle_pos_X-1, actual_turtle_pos_Y) != "dead-end"):
				turtle.forward(lireLaby.gameDict['sideL'])
				# commands.append['b']
				actual_turtle_pos_X, actual_turtle_pos_Y = fonctions.pixel2cell()				
				moveCount += 1
			for _ in range(moveCount):	
				commands.append('a')
			left, right, top, bot, end = fonctions.guidedExploration()
			if left == True and right == False and top == True and bot == False:
				turtle.right(90)
				commands.append('g')
			elif left == False and right == True and top == True and bot == False:
				turtle.right(270)
				commands.append('d')

			if fonctions.typeCellule(actual_turtle_pos_X-1, actual_turtle_pos_Y) == "crossing":
				commands.append('checkpoint')
				if right == True:
					choices += 1
				if bot == True:
					choices += 1
				if left == True:
					choices += 1
				commands.append(choices)
				way = random.randint(1, choices)
				if way == 1:
					if right == True:
						commands.append('g')
						turtle.right(270)
						commands.append('a')
						turtle.forward(lireLaby.gameDict['sidel'])
					else:
						commands.append('a')
						turtle.forward(lireLaby.gameDict['sideL'])
				elif way == 2:
					if bot == True:
						commands.append('a')
						turtle.forward(lireLaby.gameDict['sideL'])
					else:
						commands.append('d')
						turtle.right(90)
						commands.append('a')
						turtle.forward(lireLaby.gameDict['sidel'])
				elif way == 3:
					if left == True:
						commands.append('d')
						turtle.right(90)
						commands.append('a')
						turtle.forward(lireLaby.gameDict['sidel'])
					else:
						commands.append('g')
						turtle.right(270)
						commands.append('a')
						turtle.forward(lireLaby.gameDict['sidel'])

			elif fonctions.typeCellule(actual_turtle_pos_X-1, actual_turtle_pos_Y) == "dead-end":
				count = 0
				indice = len(commands) - 1
				search = len(commands) - 1
				while commands[indice] != "checkpoint":
					indice -= 1
					count += 1
				while commands[search] != "checkpoint":

					if turtle.heading() == 0: #droite
						print("bas droite")
						if commands[search] == 'a':
							turtle.forward(-(lireLaby.gameDict['sidel']))
						elif commands[search] == 'd':
							turtle.right(270)
						elif commands[search] == 'g':
							turtle.right(90)

					elif turtle.heading() == 180: #gauche
						print("bas gauche")
						if commands[search] == 'a':
							turtle.forward(-(lireLaby.gameDict['sidel']))
						elif commands[search] == 'd':
							turtle.right(270)
						elif commands[search] == 'g':
							turtle.right(90)

					elif turtle.heading() == 90: #haut
						print("bas haut")
						if commands[search] == 'a':
							turtle.forward(-(lireLaby.gameDict['sideL']))
						elif commands[search] == 'd':
							turtle.right(270)
						elif commands[search] == 'g':
							turtle.right(90)

					elif turtle.heading() == 270: #bas
						print("bas bas")
						if commands[search] == 'a':
							turtle.forward(-(lireLaby.gameDict['sideL']))
						elif commands[search] == 'd':
							turtle.right(90)
						elif commands[search] == 'g':
							turtle.right(270)
					
					commands.pop()
					search -= 1

			if fonctions.typeCelUnic(actual_turtle_pos_X-1, actual_turtle_pos_Y+1) == "exit":
				turtle.forward(lireLaby.gameDict['sideL'])

	
	print(commands)





	if fonctions.pixel2cell()[1] == exit[0] and fonctions.pixel2cell()[0] == exit[1] + 1:
		turtle.bgpic('among.gif') # end picture

	turtle.mainloop()
	return "Congratulations, you won ! "
