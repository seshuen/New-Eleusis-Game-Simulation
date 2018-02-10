"""
CMSC 671 Artificial Intelligence
The Game of New Eleusis - Phase 2
Team: Anonymous Agents
Seshagopalan Narasimhan XP27536
Rashmi Prava Patro AK14498
Rashmi Kunchakuri GV78738
"""
"""
1) http://www.onlamp.com/pub/a/python/2006/02/09/ai_decision_trees.html?page=3
2) https://stackoverflow.com/questions/6521892/how-to-access-a-dictionary-key-value-present-inside-a-list
3) https://alexlouden.com/posts/2015-defaultdict-in-python.html
4) https://www.tutorialspoint.com/python/python_dictionary.htm
5) https://stackoverflow.com/questions/1388818/how-can-i-compare-two-lists-in-python-and-return-matches


"""
import random
"""
Generating cards:
1>Generating cards randomly to observe and comprehend the hypothesis
2>Generating cards.based on the hypothesis formed-
using the same function to generate random cards and then testing the card with our own hypothesis before playing the card
"""


def generateCard():
	"""number on cards, card_num = [A,2,3,4,5,6,7,8,9,10,J,Q,K]"""
	card_num = list()
	card_suit = ['C','D','H','S']

	num = 1
	"""generating a deck of 52 cards and the returning a random card"""
	"""Defining the face cards using their corresponding values makes it easier for us to generate cards based on the hypothesis we are going to test """
	while (num <= 13):
		if (num == 1):
			letter = 'A'
		elif (num == 11):
			letter = 'J'
		elif (num == 12):
			letter = 'Q'
		elif (num == 13):
			letter = 'K'
		else:
			letter = num
		card_num.append(letter)
		num += 1

	final_card = []
	for suit in card_suit:
		for number in card_num:
			card = str(number)+suit
			final_card.append(card)
	return random.choice(final_card)
