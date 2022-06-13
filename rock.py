
import random

print("This is a simple game of Rock, Paper, Scissors")

R = 'Rock'
P = 'Paper'
S = 'Scissors'
options = [ 'R' , 'P' , 'S' ]


print("The rules of the game are: \n 1. Each player makes a choice of R or P or S representing  Rock, Paper or Scissors respectively. \n 2. Rock beats Scissors. \n 3. Paper beats Rock. \n 4. Scissors beats Paper. \n 5. If the two players choose the same “character” it’s a tie, and the game repeats")


def game():		
	move = False
	while move == False:
		try:
			player = input("Make your move?: Rock(R), Paper(P), Scissors(S) \n")
			if (player == "R" or player == "P" or player=="S"):
				move = True
		except:
			print("Value error")
			move = False
			
	CPU = random.choice(options)
			
	print("Player (%s) : CPU (%s)" %(player,CPU))
		
	
	
	if (CPU == 'R' and player  == 'S'
	or CPU == 'P' and player  == 'R' or CPU == 'S' and player  == 'P'):
		
			print ('Computer wins!')
			
	elif (CPU == player ):
		print("It's a tie!")
		game()
			
	else:
		print ('Player wins!')
		
	
game()
