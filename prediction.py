"""warning this game is based purely on chance
just like you use the roll of a dice to determine your next move 
you can use this game to determine something you want to leave on chance
"""
import random
#this is a helper function
def num_to_fate(num):
	if num<0 or num>3:
		fate="invalid number"
	else:
		if num==1:
			fate="yes, definately"
		elif num==2:
			fate="Not a chance"
		elif num==3:
			fate="Depends on external factors\n Better luck next time."
	return fate


def fate_scroll(question):
	print(question)
	print()
	print("the scroll of fate is unfolding\n Your destiny is about to be unraveled")
	num=random.randrange(1,4)
	answer=num_to_fate(num)
	print("Your fate has already been written\nNo one can deny their destiny")
	print()
	print("the scroll says...")
	return answer

print(fate_scroll("Will my dreams come true?"))