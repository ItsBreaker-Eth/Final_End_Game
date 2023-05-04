import random



def main():
	print("Welcome to the cave, you have been chosen from your peers to venture in, \nfind the magic stone, and exit the cave safely without losing the stone.")
	print('This your menu, its callable any time by typing "M"')
	
	menu = ("""
	||||||||||||||||
	|Menu ------- M|
	|Move Up ---- U|
	|Move Down -- D|
	|Move Left -- L|
	|Move Right - R|
	|Grab Stone - G|
	|Drop Stone - S|
	|Check Cord - C|
	|Quit Game -- Q|
	||||||||||||||||""")
	print(f"{menu}")

	print("You start at (0,0) Up and Down are Y values, Left and Right are X Values.")
	print("The time has begun for you to begin on your venture through The Maze, good luck, I hope to see you soon.")

	XCord = 0
	YCord = 0
	Cord = (f"({XCord}, {YCord})")
	juice = 0
	
	# Up = YCord += 1
	# Down = YCord -= 1
	# Left = XCord += 1
	# Right = XCord -= 1
	walls = []
	while juice < 30:
		temp1 = random.randrange(0,101)
		temp2 = random.randrange(0,101)
		coords = (temp1, temp2)
		walls.append(coords)
		juice += 1


	choice = None

	a = random.randint(1,100)
	b = random.randint(1,100)
	stone_location = (f"{a},{b}")

	stone = False
	spider = 0

	while choice != "Q":
		
		choice = input("What is your choice?\n")
		choice = choice.upper()

		if choice == "M":
			print(menu)
		
		elif choice == "U":
			print("You Moved Up")
			YCord += 1
			if Cord in walls:
				YCord -= 1
		elif choice == "D":
			print("You Moved Down")
			YCord -= 1
			if Cord in walls:
				YCord += 1
		elif choice == "L":
			print("You Moved Left")
			XCord += 1
			if Cord in walls:
				XCord -= 1
		elif choice == "R":
			print("You Moved Right")
			XCord -= 1
			if Cord in walls:
				XCord += 1
		elif choice == "G":
			if XCord == a and YCord == b:
				stone = True
				print("You successfully found the Stone! Try and return safely...")
			else:
				print("You are not in the right location! You crabbed a spider...")
				spider += 1
		elif choice == "S":
			if stone is True:
				stone = False
				print("You absolute idiot, the stone is magic and teleported away when you dropped it.\nGo find it again.")
			else:
				stone = True
				print("Just like in math two negatives equal a positive. \nYou found the stone! \nReturn Safely!")
		elif choice == "C":
			print((f"({XCord}, {YCord})"))
		elif choice == "W":
			print(walls)
		else:
			print("That wasn't an option. Try Again.")

		


















main()