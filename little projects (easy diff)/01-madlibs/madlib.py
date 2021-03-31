#youtuber = "mrdc1790"

#print("subscribe to " + youtuber)
#print("subscribe to {}".format(youtuber))
#print(f"subscribe to {youtuber}")

from samples import hp, code, zombie, hungergames
import random

if __name__ == "__main__":
	m = random.choice([hp, code, zombie, hungergames])
	m.madlib()