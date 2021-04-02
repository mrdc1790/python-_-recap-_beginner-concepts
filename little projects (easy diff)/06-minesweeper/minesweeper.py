import random

# let's create a board object to represent the minesweeper game - OOP
# this is so that we can just say "create a new board object," or
# "dig here", or "render this game for this object"

class Board:
	def __init__(self, dimension_size, num_bombs):
		# let's keep track of these parameters. they'll be helpful later
		self.dimension_size = dimension_size
		self.num_bombs = num_bombs

		# let's create the board
		# helper function!
		self.board = self.make_board() # plant the bombs

		# initialize a set to keep track of which locations we've uncovered
		# we'll save (row, col) tuples into this set
		self.dug = set() # if we dig at 0, 0, then self.dug = {(0,0)}

	def make_new_board(self):
		# construct a new board based on the dim size of num bombs we should construct the list of lists here (or whatever representation you prefer, 
		# but since we have a 2D board, list of lists is more natural)

		# generate a new board
		board = [[None for _ in range(self.dimension_size)] for _ in range(self.dimension_size)]
		# this creates an array like this:
		# [ [None, None, ..., None],
		#   [None, None, ..., None],
		#   [None, None, ..., None],
		#   [None, None, ..., None] ]
		# we can see how this represents a board!

		bombs_planted = 0
		while bombs_planted < self.num_bombs:
			loc = random.randint(0, self.dimension_size**2 -1)

def play(dimension_size=10, num_bombs=10):
	# Step 1: create the board and plant the bombs
	# Step 2: show the user the board and ask for where they want to dig
	# Step 3a: if location is a bomb, show game over message
	# Step 3b: if location is not a bomb, dig recursively until each square is at least NEXT to a bomb
	# Step 4: repeat steps 2 and 3a/b until there are no more spaces to dig -> VICTORY!
	pass