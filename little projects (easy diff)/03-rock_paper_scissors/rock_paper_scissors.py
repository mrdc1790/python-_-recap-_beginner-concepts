import random

def play():
	user = ""
	while True:
		user = input("'r': rock, 'p': paper, 's': scissors\n").lower()
		if user == "r" or user == "p" or user == "s":
			computer = random.choice(['r','p','s'])
			print(computer)
			if user == computer:
				print('It\'s a tie')
				return
			if is_win(user, computer):
				print("You won!")
				return True
			print(f"You lost! {computer} beats {user}")
			return False 	

		else:
			print("try again")
	

def is_win(player, opponent):
	if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
		return True

def replay():
    return input("Do you want to play again? Enter Yes or No: ").lower().startswith('y')

print("Welcome to Rock Paper & Scissors!")
game_on = True
Player_Tally = 0
Computer_Tally = 0
Tie = 0
while game_on==True:
	result = play()
	if (result == True):
		Player_Tally+=1
	elif (result == False):
	    Computer_Tally+=1
	else:
		Tie+=1    	
	if not replay():
		print(f"Player's wins: {Player_Tally}.\n Computer's wins: {Computer_Tally}.\n Ties: {Tie}.")
		break