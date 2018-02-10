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
import new_eleusis
from boardState import *

class God:

	ruleExpression = None
	ruleTree = None
	""" Set the current rule using functions from new_eleusis.py"""
	def setRule(self, expression):
		self.ruleExpression = expression
		self.ruleTree = new_eleusis.parse(expression)

	def rule(self):
		""" Return the current(actual) rule """
		return self.ruleExpression

	def __validate__(self, cards):
		return self.ruleTree.evaluate(cards)

		
