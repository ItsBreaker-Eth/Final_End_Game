def menu():
	print("""MENU
	0 - Restart
	1 - Go Home
	2 - Show Backpack
	3 - Take Off Backpack
	4 - Change Name
	5 - Display Intro
	""")

	choice = 7
	while choice not in range(6):
		try:
			choice = int(input("Choose an option:\n"))
		except:
			print("That wasn't a number.")
	return choice

intro = """
________________________Welcome to Vexatia________________________
A city in the 1600s that is shrouded in mystery and danger. 
This bustling metropolis was once a thriving hub of trade and culture, 
but something sinister has taken root beneath its surface. 
Unbeknownst to its human inhabitants, a highly advanced society of 
robotic beings has infiltrated the city and begun to exert its influence.

As the player of this text-based game, you are a time traveler from 
the year 2026 who has stumbled upon this secret plot to take over Vexatia. 
Your mission is to remain hidden and navigate the city's treacherous streets, 
uncovering clues and gathering information about the robotic threat. 
As you delve deeper into the mystery, you will encounter various characters, 
both human and robotic, who may help or hinder your progress.

However, the stakes are high, and the slightest misstep could mean the 
end of your mission - and perhaps even the end of the world as we know 
it. Can you outwit the robotic beings and save Vexatia from their clutches? 
The fate of the city and its inhabitants rests in your hands.
"""

print(intro)

skip_intro = "a"
choice_accepted = "Yes" "No" "yes" "no" 
yes = "Yes" "yes"
no = "No" "no"
instructions = """
The game is simple, you can either move North, East, South, West.
Only move in a direction using the first letter, example: N, E, S, W

Your goal in this game is to stop the robotic beings from taking over Vexatia 
by completing a series of tasks in a specific order. Failure to complete any 
of these tasks will result in the player's death and a game over. 

The tasks are as follows:

1 - Find the underground lair of the robotic beings.
2 - Retrieve a key to the lair from a secret location in the city.
3 - Hack into the lair's security system to gain access.
4 - Disable the main power source to the lair.
5 - Locate and retrieve the prototype device that the robotic beings are 
	using to control the city.
6 - Destroy the prototype device.
7 - Escape from the lair before it self-destructs.
8 - Return to your time machine and travel back to 2026.

Each of these tasks requires careful planning and execution, as well as 
navigating through the city's various obstacles and enemies. You must explore 
Vexatia thoroughly, gather information from its inhabitants, and use your wits 
and skills to overcome the challenges that lie ahead. 
Good luck, time traveler - the fate of Vexatia rests in your hands."""

while skip_intro not in choice_accepted:
	try:
		skip_intro = input("""Would You Like To Skip Intro? \nYes or No\n""")
	except:
		print("That wasn't an option!")

if skip_intro is no:
	print(instructions)


	
	 
		

