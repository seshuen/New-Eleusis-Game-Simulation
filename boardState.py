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
"""
Class: Board State
Description: Consist of all operations related to board state of the game.
Functions:
    legal(card), illegal(card), __str__(), displayBoard()
"""
class boardState:
    def __init__(self):
        # Declare an empty boardState
        self.boardState = []
        self.cardList = {}
        self.lst = []

    def legal(self, card):
        """
        # Function: legal()
        # Returns the updated boardState
        """
        # If legal append the card to the list with empty sideline
        self.boardState.append([card, []])
        # Append card to cardList
        self.cardList = {}
        self.cardList[card] = "Legal"
        self.lst.append(self.cardList)

    def illegal(self, card):
        """
        # Function: illegal()
        # Returns the updated boardState
        """
        # If illegal append the card to the list of previous play
        self.boardState[-1][1].append(str(card))
        # Append card to cardList
        self.cardList = {}
        self.cardList[card] = "Illegal"
        self.lst.append(self.cardList)

    def __str__(self):
        """
        Function that shall return the list of dictionaries representation of board state
        For ex. [['3H', []], ['9S',['JD']]] => ['3H', '9S', 'JD']
        """
        return self.lst

    def displayBoard(self):
        return self.boardState
    
