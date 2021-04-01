# let's create a board object to represent the minesweeper game - OOP
# this is so that we can just say "create a new board object," or
# "dig here", or "render this game for this object"

class Board:
	def __init__(self, dimension_size, num_bombs):
		# let's keep track of these parameters. they'll be helpful later
		self.dimension_size = dimension_size
		self.num_bombs = num_bombs

def play(dimension_size=10, num_bombs=10):
	# Step 1: create the board and plant the bombs
	# Step 2: show the user the board and ask for where they want to dig
	# Step 3a: if location is a bomb, show game over message
	# Step 3b: if location is not a bomb, dig recursively until each square is at least NEXT to a bomb
	# Step 4: repeat steps 2 and 3a/b until there are no more spaces to dig -> VICTORY!
	pass