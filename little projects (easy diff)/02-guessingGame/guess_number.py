import random

def guess(y):
	random_number = random.randint(1, y)
	guess = 0
	while guess != random_number:
		guess = int(input(f"Guess a number between 1 and {y}: "))
		if guess < random_number:
			print("Sorry, guess again. Too low.")
		elif guess > random_number:
			print("Sorry, guess again. Too high.")
		else:
			print("Congratulations! You won!")
	
y = int(input("Please input a range to play on: "))
guess(y)